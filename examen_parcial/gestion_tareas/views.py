import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from gestion_tareas.models import tarea, usuario
from datetime import date, datetime
from dateutil.parser import parse
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
    total_tareas = tarea.objects.all()

    return render(request,'gestion_tareas/dashboard.html',{
        'total_tareas':total_tareas
    })

def crearTarea(request):
    if request.method == 'POST':
        nombreTarea = request.POST.get('nombreTarea')
        fechaCreacion = request.POST.get('fechaCreacion')
        #print(type(fechaCreacion))
        fechaEntrega = request.POST.get('fechaEntrega')
        #print(type(fechaEntrega))
        #print(type(fechaEntrega), type(date.today()))
        #print(fechaEntrega, date.today())
        fechaEntrega = datetime.strptime(fechaEntrega, '%Y-%m-%d').date()
        #print(type(fechaEntrega))
        #print(type(fechaEntrega), type(date.today()))        
        responsableTarea = request.POST.get('responsableTarea')

        delta = fechaEntrega - date.today()
        #print("days delta vale: ",delta.days)
        #print("LA FECHA DE ENTREGA ES: ", fechaEntrega.day)
        if delta.days >= 3:
            estadoTarea = 'PROGRESO'
        elif  delta.days >= 0 and delta.days <= 3:
            estadoTarea = 'FINALIZANDO'
        elif delta.days < 0:
            estadoTarea = 'PENDIENTE'
        else:
            estadoTarea = 'FALLIDO'

        tarea(descripcion=nombreTarea,fecha_creacion=fechaCreacion,fecha_entrega=fechaEntrega,responsable=responsableTarea,estado=estadoTarea).save()

        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))

    return render(request,'gestion_tareas/crear_tarea.html')

def detalleTarea(request,id):
    tarea_detalle = tarea.objects.filter(id=id)
    return render(request,'gestion_tareas/detalleTarea.html',{
        'tarea_detalle':tarea_detalle
    })
# filter() will always give you a QuerySet" - it's iterable
# get() return single object and it's not iterable
# Basically use get() when you want to get a single unique object, 
# and filter() when you want to get all objects that match your lookup parameters.
def editarTarea(request,id):
    tarea_a_editar = tarea.objects.get(id=id)

    if request.method == 'POST':
        nombreTarea = request.POST.get('nombreTarea')
        fechaCreacion = request.POST.get('fechaCreacion')
        fechaEntrega = request.POST.get('fechaEntrega')
        fechaEntrega = datetime.strptime(fechaEntrega, '%Y-%m-%d').date()
        delta = fechaEntrega - date.today()
        if delta.days >= 3:
            estadoTarea = 'PROGRESO'
        elif  delta.days >= 0 and delta.days <= 3:
            estadoTarea = 'FINALIZANDO'
        elif delta.days < 0:
            estadoTarea = 'PENDIENTE'
        else:
            estadoTarea = 'FALLIDO'

        responsableTarea = request.POST.get('responsableTarea')
        tarea_a_editar.descripcion = nombreTarea
        tarea_a_editar.fecha_creacion = fechaCreacion
        tarea_a_editar.fecha_entrega = fechaEntrega
        tarea_a_editar.responsable = responsableTarea
        tarea_a_editar.estado = estadoTarea
        tarea_a_editar.save()

        
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))


    return render(request,'gestion_tareas/editarTarea.html',{
        'tarea_a_editar': tarea_a_editar
    })

def eliminarTarea(request,id):

    tarea.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))

def finalizarTarea(request,id):
    tarea_a_editar = tarea.objects.get(id=id)
    tarea_a_editar.estado = 'FINALIZADO'
    tarea_a_editar.save()
    return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))