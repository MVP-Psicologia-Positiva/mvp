from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserForm, LuluTrainningForm
from lulu_teacher import models


# Create your views here.

def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def view_lulu(request):
    return render(request, 'lulu.html')

def view_training_files(request):
    return render(request, 'trainingFiles.html')

def view_home(request):
    return render(request, 'home.html')

def view_register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('register')
    else:
        form = CustomUserForm()
    
    users = User.objects.all() 
    return render(request, 'register.html', {'form': form, 'users': users})

def training_list(request):
    if request.method == 'POST':
        form = LuluTrainningForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('training_list')  # Redireciona para a mesma página
    else:
        form = LuluTrainningForm()

    trainings = models.luluTrainning.objects.all()
    return render(request, 'trainingFiles.html', {'form': form, 'trainings': trainings})

