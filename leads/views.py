from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
#Biblioteca de django que permite crear una coockie para la sesión del usuario
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError



# Create your views here.
def home (request):
    return render(request, 'index.html')

def signin (request):
    if request.method == 'GET':
        return render(request, 'login.html',{
        'form': AuthenticationForm
        })
    else:
        user=authenticate (
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'El nombre o la contraseña son incorrectos'
        })
        else:
            login(request, user)
            return redirect('accion')
        
def salir(request):
    logout(request)
    return redirect('index')
        
def accion(request):
    return render(request, 'accion.html')

