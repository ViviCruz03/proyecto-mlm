from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
#Biblioteca de django que permite crear una coockie para la sesión del usuario
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import *  # Importar el modelo para los estados
from django.contrib.auth.decorators import login_required



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

@login_required        
def salir(request):
    logout(request)
    return redirect('index')
        
@login_required
def accion(request):
    return render(request, 'accion.html')

@login_required
def crearConsulta(request):
    return render(request, 'consulta1.html',{'estados': Estado.ESTADOS})

@login_required
def consulta2(request):
    return render(request, 'consulta2.html',{"UniEconomicas": UniEconomicas})

@login_required
def segConsulta(request):
    return render(request, 'seguimiento1.html')


@login_required
def dash(request):
    return render(request, 'dash.html')

