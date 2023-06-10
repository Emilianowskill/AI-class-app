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
	title = models.CharField(max_length=20, help_text="ingrese el titulo del algoritmo (max 20)")
	summary = models.TextField(max_length=300, help_text="Ingrese una descripción del algoritmo (max 200")
	logo = models.ImageField(height_field=None, width_field=None, max_length=100,help_text="Ingrese un icono para el algoritmo")

	def __str__(self):
		"""String que representa al objeto algoritmo"""
		return self.title

	def get_logo_image(self):
		return self.logo

	def get_absolute_url(self):
		"""Devuelve el URL a una instancia particular de algoritmos"""
		return reverse('algoritmo-detail', args=[str(self.id)])

class Genre(models.Model):
	"""
	Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
	"""
	name = models.CharField(max_length=200, help_text="Ingrese el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)")

	def __str__(self):
		"""
		Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
		"""
		return self.name

class Book(models.Model):
	"""
	Modelo que representa un libro (pero no un Ejemplar específico).
	"""

	title = models.CharField(max_length=200)

	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	# ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
	# 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.

	summary = models.TextField(max_length=1000, help_text="Ingrese una breve descripción del libro")

	isbn = models.CharField('ISBN',max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

	genre = models.ManyToManyField(Genre, help_text="Seleccione un genero para este libro")
	# ManyToManyField, porque un género puede contener muchos libros y un libro puede cubrir varios géneros.
	# La clase Genre ya ha sido definida, entonces podemos especificar el objeto arriba.

	def __str__(self):
		"""
		String que representa al objeto Book
		"""
		return self.title


	def get_absolute_url(self):
		"""
		Devuelve el URL a una instancia particular de Book
		"""
		return reverse('book-detail', args=[str(self.id)])

import uuid # Requerida para las instancias de libros únicos

class BookInstance(models.Model):
	"""
	Modelo que representa una copia específica de un libro (i.e. que puede ser prestado por la biblioteca).
	"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)

	status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')

	class Meta:
		ordering = ["due_back"]


	def __str__(self):
		"""
		String para representar el Objeto del Modelo
		"""
		return '%s (%s)' % (self.id,self.book.title)

class Author(models.Model):
	"""
	Modelo que representa un autor
 	"""
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	def get_absolute_url(self):
		"""
		Retorna la url para acceder a una instancia particular de un autor.
		"""
		return reverse('author-detail', args=[str(self.id)])


	def __str__(self):
		"""
		String para representar el Objeto Modelo
		"""
		return '%s, %s' % (self.last_name, self.first_name)