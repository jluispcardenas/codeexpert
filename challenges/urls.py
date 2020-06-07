from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path(
        route='',
        view=cache_page(views.HomeView.as_view(), 60 * 15),
        name='home'),

    path(
        route='search',
        view=views.SearchView.as_view(),
        name='search'),

    path(
        route='category/<int:id>/<str:slug>',
        view=views.SearchView.as_view(),
        name='category'),

    path(
        route='submit_answer',
        view=views.submit_answer,
        name='submit_answer'
    ),

    path(
        route='<int:id>/<str:slug>/',
        view=views.ItemView.as_view(),
        name='item')
]
