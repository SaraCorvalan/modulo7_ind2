# Generated by Django 4.2.4 on 2023-08-13 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0003_alter_registrotareas_fecha_vencimiento_tarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrotareas',
            name='fecha_vencimiento_tarea',
            field=models.DateTimeField(verbose_name='Fecha vencimiento de tarea'),
        ),
    ]
