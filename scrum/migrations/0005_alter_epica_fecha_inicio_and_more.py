# Generated by Django 4.2 on 2024-10-24 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0004_alter_epica_fecha_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epica',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
