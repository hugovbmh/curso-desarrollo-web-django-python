from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from gestion_tareas.models import tarea, usuario

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
        fechaEntrega = request.POST.get('fechaEntrega')
        responsableTarea = request.POST.get('responsableTarea')
        estadoTarea = request.POST.get('estadoTarea')

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
        responsableTarea = request.POST.get('responsableTarea')
        estadoTarea = request.POST.get('estadoTarea')
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