# Generated by Django 4.2.4 on 2023-08-13 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrotareas',
            name='descripcion_tarea',
            field=models.CharField(max_length=150, verbose_name='Descripción de tarea'),
        ),
        migrations.AlterField(
            model_name='registrotareas',
            name='estado_tarea',
            field=models.CharField(choices=[('1', 'Pendiente'), ('2', 'En progreso'), ('3', 'Completada')], default='1', max_length=1, verbose_name='Estado de tarea'),
        ),
        migrations.AlterField(
            model_name='registrotareas',
            name='fecha_vencimiento_tarea',
            field=models.DateTimeField(verbose_name='Fecha vencimiento de tarea'),
        ),
        migrations.AlterField(
            model_name='registrotareas',
            name='titulo_tarea',
            field=models.CharField(max_length=50, verbose_name='Título de tarea'),
        ),
    ]
