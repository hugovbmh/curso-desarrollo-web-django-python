from . import views
from django.urls import path

app_name = 'gestion_tareas'

urlpatterns = [
    path('',views.ingreso,name='ingreso'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('eliminarTarea/<str:id>',views.eliminarTarea,name='eliminarTarea'),
    path('crearTarea',views.crearTarea,name='crearTarea'),
    path('detalleTarea/<str:id>',views.detalleTarea,name='detalleTarea'),
    path('editarTarea/<str:id>',views.editarTarea,name='editarTarea')
]