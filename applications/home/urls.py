from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('prueba/',views.PruebaView.as_view()),
    path('lista/',views.PruebaLista.as_view()),
    path('listaprueba/',views.ListaPrueba.as_view()),
    path('create/',views.PruebaCreate.as_view()),
    
    ]