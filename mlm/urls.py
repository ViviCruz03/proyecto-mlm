"""
URL configuration for mlm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from leads import views

urlpatterns = [
    path('', include('leads.urls')),

    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.signin, name='login'),
    path('salir/', views.salir, name='salir'),

    # ------- SUPERVISORES --------------
    path('accionSup/', views.accionSup, name='accionSup'),
    path('consulta1/',views.consulta1, name='consulta1'),
    path('consulta2/', views.consulta2,name='consulta2'),
    path('verAsesor/', views.verAsesor, name='verAsesor'),
    path('segConsulta/',views.segConsulta, name='seg_consulta' ),
    path('dashSup/', views.dashSup, name='dashSup'),

    #-----------ASESORES --------------
    path('accionAs/',views.accionAs, name='accionAs'),
    path('segAs1/',views.segAs1, name='segAs1'),
    path('dashAses/',views.dashAses, name='dashAses')
    ]
