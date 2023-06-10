from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, UserProfile, Files, Algoritmo

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(UserProfile)
admin.site.register(Files)
admin.site.register(Algoritmo)
