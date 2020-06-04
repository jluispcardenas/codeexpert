from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import FormView, DetailView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import SignupForm
from challenges.models import Challenge, Answer

class PanelView(ListView):
    template_name = 'profiles/panel.html'
    model = None
    context_object_name = 'challenges'

    def get_queryset(self):
        challenges = Answer.objects.filter(user=self.request.user, valid=True).values_list('challenge_id', flat=True)
        queryset = Challenge.objects.filter(pk__in=challenges, active=True)

        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        
        return context 

class UserView(DetailView):
    template_name = 'profiles/user.html'
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'slug'
    context_object_name = 'profile'

class SignupUserView(FormView):
    form_class = SignupForm
    template_name = "profiles/signup.html"
    success_url = reverse_lazy("profiles:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginUserView(LoginView):
    template_name = "profiles/login.html"

class LogoutUserView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy("profiles:login")


