from random import choices
from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50, null=False)
    
    class Meta:
        ordering = ('id',)
        verbose_name = ('Habilidades')
        verbose_name_plural = ('Habilidades Empleados')
    
    def __str__(self):
        return str(self.id) + ' - ' +(self.habilidad)


class Empleado(models.Model):
    job_choices = (
        ('0','Otro'),
        ('1','Contador'),
        ('2','Administrador'),
        ('3','Vendedor'),
        ('4','RR.HH'),
        )
    
    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField('Nombre Completo', max_length=120, blank=True, null=True)
    job = models.CharField('Puesto', choices=job_choices, max_length=1)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True) 
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField(blank=True)



    class Meta:
        ordering = ['departamento']
        verbose_name = ('Lista Personal')
        verbose_name_plural = ('Empleados')    
    
    
    def __str__(self):
        return str(self.departamento.shor_name)+ ' - ' + self.first_name + ' - ' + self.last_name