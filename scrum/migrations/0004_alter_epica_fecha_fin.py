# Generated by Django 4.2 on 2024-10-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0003_alter_epica_fecha_fin_alter_epica_fecha_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epica',
            name='fecha_fin',
            field=models.DateField(blank=True, null=True),
        ),
    ]
