# Generated by Django 4.0.5 on 2022-09-06 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tareas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='tarea_usuario',
            new_name='responsable',
        ),
    ]
