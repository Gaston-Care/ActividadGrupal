# Generated by Django 4.2 on 2024-10-22 18:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scrum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='backlog_sprint',
            field=models.ManyToManyField(blank=True, to='scrum.tarea'),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='equipo_desarrollo',
            field=models.ManyToManyField(blank=True, related_name='sprints', to=settings.AUTH_USER_MODEL),
        ),
    ]