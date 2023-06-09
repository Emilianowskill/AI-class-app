from django.contrib import admin
from ai_class_app import models

admin.site.register(models.UserProfile)
admin.site.register(models.Files)