from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_login),
    path('home', views.view_home, name='home'),
    path('register', views.view_register, name='register'),
    path('lulu-a', views.view_lulu_a),
    path('lulu-b', views.view_lulu_b),
    path('trainingFiles', views.view_training_files)
]