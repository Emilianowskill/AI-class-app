# Generated by Django 3.2.19 on 2023-06-10 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_class_app', '0002_alter_algoritmo_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algoritmo',
            name='logo',
            field=models.ImageField(help_text='Ingrese un icono para el algoritmo', upload_to=''),
        ),
        migrations.AlterField(
            model_name='algoritmo',
            name='summary',
            field=models.TextField(help_text='Ingrese una descripción del algoritmo (max 200', max_length=300),
        ),
        migrations.AlterField(
            model_name='algoritmo',
            name='title',
            field=models.CharField(help_text='ingrese el titulo del algoritmo (max 20)', max_length=20),
        ),
    ]
