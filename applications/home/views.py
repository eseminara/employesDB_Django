from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView
from .models import *
# Create your views here.

class PruebaView (TemplateView):
    template_name = 'home/prueba.html'

class PruebaLista (ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'
    queryset = ['0','10','20','30']
    

class ListaPrueba (ListView):
    template_name = 'home/listaprueba.html'
    model = Prueba
    context_object_name = 'listaprueba'
    

class PruebaCreate(CreateView):
    model = Prueba
    template_name = 'home/create.html'
    fields = ['titulo','subtitulo','cantidad']