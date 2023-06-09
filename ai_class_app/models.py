from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.urls import reverse

class UserProfileManager(BaseUserManager):
	"""Administrador para los perfiles de usuario"""

	def create_user(self, email, name, password=None):
		"""Crea un nuevo perfil de usuario"""
		if not email:
			raise ValueError("Introduce tu correo electrónico")

		email = self.normalize_email(email)
		user = self.model(email=email, name=name)

		user.set_password(password)
		user.save(using=self._db)

		return user


	def create_superuser(self, email, name, password):
		"""Crea un nuevo super-perfil"""
		user = self.create_user(email, name, password)

		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)

		return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""Modelo de base de datos para los usuarios en el sistema"""
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		"""Obtiene el nombre completo del usuario"""
		return self.name

	def get_short_name(self):
		"""Obtiene el nombre corto del usuario"""
		return self.name

	def __str__(self):
		"""Regrese el string que representa al usuario"""
		return self.email

class Files(models.Model):
	archivo = models.FileField(max_length=250, null=True, default=None)

	def __str__(self):
		return self.archivo

class Algoritmo(models.Model):
	title = models.CharField(max_length=200)
	summary = models.TextField(max_length=1000, help_text="Esta es una descripción del algoritmo")

	def __str__(self):
		"""String que representa al objeto algoritmo"""
		return self.title

	def get_absolute_url(self):
		"""Devuelve el URL a una instancia particular de algoritmos"""
		return reverse('algoritm-detail', args=[str(self.id)])
