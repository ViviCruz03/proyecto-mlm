from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


#choices Status de Usuarios
tipos = [
    ('1','Cliente'),
    ('2','Prospecto'),
    ('3','No prospecto'),
    ('4','Cuenta ganada'),
    ('5','Descartado')
]

#Tabla Empresa
class Empresa(models.Model):
    nombreEmp = models.CharField(max_length=200, verbose_name='Empresa')
    giro = models.CharField(max_length=200, verbose_name='Giro')
    direccionEmp = models.CharField(max_length=250, verbose_name='Dirección de la empresa')

    def __str__(self):
        return '%s, %s, %s' % (self.nombreEmp, self.giro, self.direccionEmp)
    

#Table  Sucursal
class Sucursal(models.Model):
    nombreSuc = models.CharField(max_length=200, verbose_name='Sucursal')
    direccionSuc = models.CharField(max_length=250, verbose_name='Dirección de la sucursal')
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, verbose_name='Empresa')

    def __str__(self):
        return '%s, %s, %s' %(self.nombreSuc, self.direccionSuc, self.empresa)


#Table Supervisor
class Supervisor(models.Model):
    nomSuper= models.CharField(max_length=250, verbose_name='Supervisor')
    sucursal= models.ForeignKey('Sucursal', on_delete=models.CASCADE, verbose_name='Sucursal')

    def __str__(self):
        return '%s' %(self.nomSuper)

#Table Asesor
class Asesor(models.Model):
    nomAses= models.CharField(max_length=250, verbose_name="Asesor")
    rutaAses=models.CharField(max_length=250, verbose_name='Ruta')
    supervisor=models.ForeignKey('Supervisor', on_delete=models.CASCADE, verbose_name='Supervisor')

    def __str__(self):
        return '%s, %s' %(self.nomAses, self.rutaAses)

#Table Unidades Economicas
class UniEconomicas(models.Model):
    nom_uniEc=models.CharField(max_length=250, verbose_name='Unidad económica')
    clase_uniEc=models.CharField(max_length=250, verbose_name='Clase de la unidad económica')
    codigoPos=models.CharField(max_length=5, verbose_name='Codigo postal')
    direc_uniEc=models.CharField(max_length=250, verbose_name='Dirección')
    tel_uniEc=models.CharField(max_length=20, verbose_name='Telefono', null=True)
    correp_uniEc=models.CharField(max_length=100, verbose_name='Correo', null=True)
    lat=models.CharField(max_length=50,verbose_name='Latitud')
    long=models.CharField(max_length=50,verbose_name='Longitud')
    status= models.CharField(max_length=2, choices=tipos, verbose_name='Status', default=0)
    
#Tabla Consultas
nom_Cons=models.CharField(max_length=200, verbose_name='Consulta')
fecha_Cons= models.DateField(verbose_name='Fecha', null= False)
asesor=models.ForeignKey('Asesor', on_delete=models.CASCADE, verbose_name='Asesor')
uniEc=models.ForeignKey('UniEconomicas', on_delete=models.CASCADE, verbose_name='Unidades Economicas')


    
    
