from django.urls import path
from .views import home
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('home/', views.home , name = "home"),
    path('inicio_sesion/', views.inicio_sesion , name= "inicio_sesion"),
    path('redirigir/', views.redirigir, name='redirigir'),
    path('registro_paciente/', views.registro_paciente , name= "registro_paciente"),
    path('registro_medico/', views.registro_medico , name= "registro_medico"),
    

]       
