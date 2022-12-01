from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'persona_app'

urlpatterns = [
    
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
        ),
    path(
        'list_all_empleados/',
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
        ),
    path('list_kword/',
        views.ListEmpleadoByKword.as_view(),
        ),
    path('list_habilidades/',
        views.ListEmpleadoHabilidades.as_view(),
        ),
    path('ver-empleado/<pk>',
        views.EmpleadoDetailView.as_view(),
        name='detalle'
        ),
    path('crear-empleado/',
        views.CreateEmpleado.as_view(),
        name='empleado_add'
        ),
    path(
        'success/',
        views.SuccessView.as_view(), 
        name='correcto'
        ),
    path(
        'modificar-empleado/<pk>',
        views.EmpleadoUpdate.as_view(), 
        name='modificar'
        ),
    path(
        'eliminar-empleado/<pk>',
        views.EmpleadoDelete.as_view(),
        name='eliminar'
        ),
    path(
        'list-by-area/<shorname>',
        views.ListEmpleadosByArea.as_view(),
        name='empleados_area'
        ),
    path(
        'list-admin',
        views.ListEmpleadosAdmin.as_view(),
        name='empleados_admin'
        ),

]