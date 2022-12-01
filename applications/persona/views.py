from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    )
from django.urls import reverse_lazy
from applications.departamento.models import Departamento
#Models
from .models import Empleado
#Forms
from .forms import EmpleadoForm

# Create your views here.

class InicioView(TemplateView):
    '''Pagina de inicio'''
    template_name = 'inicio.html'


class ListEmpleadosAdmin(ListView):
    template_name = 'persona/list_admin.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all_empleados.html'
    paginate_by = 4
    ordering = 'first_name'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
                full_name__icontains=palabra_clave,
                )
        #print('***********',lista)
        return lista
    

class ListEmpleadoByKword(ListView):
    template_name = 'persona/list_kword.html'
    paginate_by = 4
    ordering = 'first_name'
    
    def get_queryset(self):
        print('***********')
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
                full_name__icontains=palabra_clave,
                )
        #print('***********',lista)
        return lista
    

class ListEmpleadoHabilidades(ListView):
    template_name = 'persona/list_habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        print('***********')
        empleado = Empleado.objects.get(id=2)
        return empleado.habilidades.all()


class ListEmpleadosByArea(ListView):
    model = 'Empleado'
    template_name = "persona/list_by_area.html"
    context_object_name = 'empleados'
    
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(departamento__shor_name=area)
        return lista



class SuccessView(TemplateView):
    template_name = 'persona/success.html'


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detalle_empleado.html"
    
    def get_context_data(self, **kwargs):
        print('***********')
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context ['titulo'] = ''
        print('****DETALLE VIEW*******')
        return context


class CreateEmpleado (CreateView):
    model = Empleado
    template_name = "persona/crear-empleado.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        print('****',empleado,'*****')
        return super(CreateEmpleado, self).form_valid(form)
    


class EmpleadoUpdate(UpdateView):
    template_name = "persona/update_empleado.html"
    model = Empleado
    fields = [
            'first_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
            ]
    success_url = reverse_lazy('persona_app:empleados_admin')
    
    

class EmpleadoDelete(DeleteView):
    model = Empleado
    template_name = "persona/delete_empleado.html"
    success_url = reverse_lazy('persona_app:empleados_admin')



