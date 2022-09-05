from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from gestion_tareas.models import usuario

# Create your views here.

def ingreso(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        password = request.POST.get('password')
        #validar usuario y contraseña
        user_registrado = 0
        user_totales = usuario.objects.all()
        for user in user_totales:
            if user.nombre == nombre and user.password_usuario == password:
                user_registrado = 1
        
        if user_registrado == 1:
            return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
        else:
            return render(request,'gestion_tareas/ingreso.html',{
                'mensaje':'USUARIO NO REGISTRADO'
            })
        #fin validar

    return render(request,'gestion_tareas/ingreso.html')

def dashboard(request):


    return render(request,'gestion_tareas/dashboard.html')