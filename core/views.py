import requests
from django.shortcuts import render,redirect
from django.http import JsonResponse

def home(request):
    return render(request, 'core/home.html')


def redirigir(request):
    
    return redirect('home')  


def inicio_sesion(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'home':
            return redirect('/')  
    return render(request, 'core/inicio_sesion.html')


def registro_paciente(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'home':
            return redirect('/')
    return render(request, 'core/registro_paciente.html')



def registro_medico(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'home':
            return redirect('/')  
    return render(request, 'core/registro_medico.html')




#############COMO CONECTAR LA PINCHE API A MI DJANGO ########################3


