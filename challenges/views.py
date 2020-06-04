import os
import subprocess
import logging
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify

from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.views.generic import ListView, DetailView, View
from django.views.decorators.http import require_http_methods

from .decorators import ajax_login_required
from .models import Challenge, Category, Answer
from django.contrib.auth.models import User

from django.views.decorators.cache import cache_page

logger = logging.getLogger("challenges")

class HomeView(ListView):
    model=Challenge
    template_name="challenges/home.html"
    paginate_by = 10
    context_object_name = 'challenges'

    # filter by actives
    queryset = Challenge.objects.filter(active=True).order_by('-pk')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('name').all()
        context['winners'] = Answer.objects.filter(valid=True).select_related().order_by('-pk')[:5]
        context['completed'] = [] if not self.request.user.is_authenticated else Answer.objects.filter(user=self.request.user, valid=True).values_list('challenge_id', flat=True)

        return context

class ItemView(DetailView):
    model = Challenge
    template_name="challenges/detail.html"
    pk_url_kwarg = "id"
    context_object_name = 'challenge'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['win'] = False
        context['current_runtime'] = "python3.8"
        context['template'] = context['challenge'].template
        if self.request.user.is_authenticated:
            context['answers'] = Answer.objects.filter(user=self.request.user, challenge=context['challenge']).all()
            if context['answers']:
                context['template'] = context['answers'][len(context['answers']) -1].code
                context['win'] = context['answers'][len(context['answers']) - 1].valid
            context['current_runtime'] = self.request.user.profile.current_runtime

        return context

class SearchView(ListView):
    template_name = 'challenges/search.html'
    paginate_by = 20

    def get_queryset(self):
        challenges = Challenge.objects.order_by('-pk')
        
        cat = self.kwargs['id'] if 'id' in self.kwargs else None
        if not cat:
            cat = self.request.GET.get("cat", None)
        
        if cat:
            challenges = challenges.filter(category=cat)
        q = self.request.GET.get("q", None)
        if q:
            challenges = challenges.filter(title__icontains=q)

        return challenges

    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        cat = self.kwargs['id'] if 'id' in self.kwargs else None
        if not cat:
            cat = self.request.GET.get("cat", None)
        if cat:
            context['category'] = Category.objects.filter(pk=cat).first()
        context['categories'] = Category.objects.order_by('name').all()
        context['completed'] = [] if not self.request.user.is_authenticated else Answer.objects.filter(user=self.request.user, valid=True).values_list('challenge_id', flat=True)

        return context

@ajax_login_required
@require_http_methods(["POST"])
def submit_answer(request):
    if request.is_ajax():
        user_id = str(request.user.id)
        challenge_id = request.POST.get("challenge_id")
        code = request.POST.get("code")
        runtime = request.POST.get("runtime") # "python3.8"
        current_runtime = request.user.profile.current_runtime #"python3.8"

        # basic validations
        if len(code) < 3:
            return JsonResponse({'errorType': 'InvalidParameter', 'errorMessage': 'El codigo no debe estar vacio'})
        if runtime not in ["nodejs12.x", "python3.8"]:
            return JsonResponse({'errorType': 'InvalidParameter', 'errorMessage': 'Runtime invalido'})

        challenge = Challenge.objects.filter(pk=challenge_id).first()
        if not challenge:
            return JsonResponse({'errorType': 'InvalidParameter', 'errorMessage': 'Invalid challenge'})

        extension = get_extension_by_runtime(runtime)
    
        # configuration
        config_memory_size = "128"
        config_timeout = "8"
        config_role = "arn:aws:iam::930379767415:role/service-role/test1-role-u851bbd3"
        config_accesskey = "AKIA5RHXUTZ3V2NAP6GW"
        config_secret = "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"
        config_region = "us-east-2"
        default_aws_access_config = "AWS_ACCESS_KEY_ID={config_accesskey} AWS_SECRET_ACCESS_KEY={config_secret} AWS_DEFAULT_REGION={config_region}".format(config_accesskey=config_accesskey,config_secret=config_secret,config_region=config_region)

        if os.path.exists("/tmp/lambda_function_" + user_id + ".zip"):
            os.system("rm /tmp/lambda_function_" + user_id + ".zip")

        if os.path.exists("/tmp/lambda_function_" + user_id):
            os.system("mkdir /tmp/lambda_function_" + user_id)
            os.system("chmod 0777 /tmp/lambda_function_" + user_id)
        
        content = ""
        with open("/home/ubuntu/challenges/template_challenge_{challenge_id}_{runtime}.{extension}".format(challenge_id=challenge_id,runtime=runtime,extension=extension), "r") as rf:
            content = rf.read().replace("[USER_FUNCTION]", code)

        with open("/tmp/lambda_function_{user_id}/lambda_function.{extension}".format(user_id=user_id,extension=extension), "w") as wf:
            wf.write(content)
        
        check_parse = check_valid_file(user_id, runtime, extension)
        if len(check_parse) < 5:
            os.system("zip /tmp/lambda_function_{user_id}.zip -j /tmp/lambda_function_{user_id}/lambda_function.{extension}".format(user_id=user_id,extension=extension))
            
            ret = ""
            if current_runtime == "":
                ret = system_call("{default_aws_access_config} aws lambda create-function --function-name lambda_function_{user_id} --memory-size {config_memory_size} --timeout {config_timeout} --runtime {runtime} --zip-file fileb:///tmp/lambda_function_{user_id}.zip --handler lambda_function.lambda_handler  --role {config_role}".format(default_aws_access_config=default_aws_access_config,user_id=user_id,config_memory_size=config_memory_size,config_timeout=config_timeout,runtime=runtime,config_role=config_role))
                request.user.profile.current_runtime = runtime
                request.user.profile.save()
            else:
                if runtime != current_runtime:
                    os.system("{default_aws_access_config} aws lambda update-function-configuration --function-name lambda_function_{user_id} --runtime {runtime}".format(default_aws_access_config=default_aws_access_config,user_id=user_id,runtime=runtime))
                ret = system_call("{default_aws_access_config} aws lambda update-function-code --function-name lambda_function_{user_id} --zip-file fileb:///tmp/lambda_function_{user_id}.zip".format(default_aws_access_config=default_aws_access_config,user_id=user_id))
            

            if "error" in str(ret):
                return JsonResponse({'errorType': 'InternalError', 'errorMessage': 'Error al ejecutar funcion, intente mas tarde'+ret})
            else:
                ret = os.system("{default_aws_access_config} aws lambda invoke --function-name \"lambda_function_{user_id}:\$LATEST\" \"/tmp/out_{user_id}.txt\"".format(default_aws_access_config=default_aws_access_config,user_id=user_id))
            
                result = ""
                with open("/tmp/out_{user_id}.txt".format(user_id=user_id), "r") as f:
                    result = str(f.read())
                
                response = json.loads(result)
                valid = response and "errorType" not in response
                status = "Success" if response and 'errorType' not in response else response['errorType'] 
               
                updateAnswer(challenge, valid, request.user, code, status)
  
                return JsonResponse(response)
        else:
            updateAnswer(challenge, False, request.user, code, "ParseError")
            return JsonResponse({'errorType': 'ParseError', 'errorMessage': check_parse})

def updateAnswer(challenge, valid, user, code, status):
    answer = Answer.objects.create(challenge=challenge,user=user,valid=valid, code=code, status=status)
    challenge.submissions = challenge.submissions + 1
    user.profile.submissions = user.profile.submissions + 1
    if valid:
        challenge.accepted = challenge.accepted + 1
        user.profile.accepted = user.profile.accepted + 1
    
    user.profile.save()
    challenge.save()
    
def check_valid_file(user_id, runtime, extension):
    if 'python3' in runtime:
        return system_call("/usr/bin/python3 -m py_compile /tmp/lambda_function_{user_id}/lambda_function.py".format(user_id=user_id))
    elif 'python' in runtime:
        return system_call("/usr/bin/python -m py_compile /tmp/lambda_function_{user_id}/lambda_function.py".format(user_id=user_id))
    else:
        return ""    

def system_call(command):
    try:
        return str(subprocess.check_output([command], shell=True, stderr=subprocess.STDOUT))
    except subprocess.CalledProcessError as e:
        return str(e.output)

def get_extension_by_runtime(runtime):
    if 'python' in runtime:
        return 'py'
    elif 'node' in runtime:
        return 'js'
    elif 'ruby' in runtime:
        return 'rb'
    elif 'java' in runtime:
        return 'java'
    else:
        return False

