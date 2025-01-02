from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_login),
    path('home', views.view_home, name='home'),
    path('register', views.view_register, name='register'),
    path('lulu', views.view_lulu),
    path('trainingFiles', views.training_list, name='training_list')
]