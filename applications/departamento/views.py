from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import (
    ListView,
    )
from .forms import NewDepartamentoForm
from .models import Departamento
from applications.persona.models import Empleado

# Create your views here.

class NewDepartamentoView (FormView):
    template_name = 'departamento/new-departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self,form):
        print ('*****FORM_VALID*****')
        
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
        )
        depa.save()
        
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job = '1',
            departamento = depa
            )
        return super(NewDepartamentoView, self).form_valid()



class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'