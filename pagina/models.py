# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Proyecto(models.Model):
	nombre = models.CharField(max_length = 60)

class Actividad(models.Model):
	nombre = models.CharField(max_length = 60)
	usuario = models.ForeignKey(User, blank=True, null=True)
	fecha_creacion =  models.DateTimeField(auto_now_add = True)
	fecha_fin = models.DateTimeField(null = True, blank = True)
	prioridad = models.PositiveSmallIntegerField(default = 0)
	dificultad = models.PositiveSmallIntegerField(default = 0)
	project = models.ForeignKey(Proyecto, null = True, blank = True)

	def set_done(self):
		self.fecha_fin = datetime.now()

	def set_open(self):
		self.fecha_fin = None

	def prioridad_str(self):
		if self.prioridad == 0:
			return "Baja"

		if self.prioridad == 1:
			return "Normal"

		if self.prioridad == 2:
			return "Alta"

		return "Sin definir"

	def difficulty_str(self):
		if self.dificultad == 0:
			return u"Muy fácil"

		if self.dificultad == 1:
			return u"Fácil"

		if self.dificultad == 2:
			return u"Normal"

		if self.dificultad == 3:
			return u"Difícil"

		if self.dificultad == 4:
			return u"Muy difícil"

		return "Sin definir"

	def project_str(self):
		if self.project == None:
			return "Sin definir"

		return self.project.name

	def usuario_str(self):
		if self.user == None:
			return "Todo el mundo"

		return self.usuario.username
