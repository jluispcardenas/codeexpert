from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from functools import wraps

def ajax_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.is_ajax():
            if not request.user.is_authenticated:
                return JsonResponse({'error': "Unauthenticated"}, status=401)
        else:
            if request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            else:
                return  redirect(reverse_lazy('login'))
    return wrapper