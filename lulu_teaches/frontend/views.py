from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserForm

# Create your views here.
def view_lulu_a(request):
    return render(request, 'lulu-a.html')

def view_lulu_b(request):
    return render(request, 'lulu-b.html')

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

@login_required
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

