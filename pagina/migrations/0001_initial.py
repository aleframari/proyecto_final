# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_fin', models.DateTimeField(null=True, blank=True)),
                ('prioridad', models.PositiveSmallIntegerField(default=0)),
                ('dificultad', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='actividad',
            name='project',
            field=models.ForeignKey(null=True, blank=True, to='pagina.Proyecto'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='usuario',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
