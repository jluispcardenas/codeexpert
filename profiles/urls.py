from django.urls import path

from . import views

urlpatterns = [
    path(route='panel',
        view=views.PanelView.as_view(),
        name='panel'),

    path(route='user/<str:slug>',
        view=views.UserView.as_view(),
        name='user'),

    path(
        route='login',
        view=views.LoginUserView.as_view(),
        name='login'),
      ]

"""
    path(
        route='signup/',
        view=views.SignupUserView.as_view(),
        name='signup'),
    
  
    path(
        route='logout/',
        view=views.LogoutUserView.as_view(),
        name='logout')"""