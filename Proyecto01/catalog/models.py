from django.db import models

class modelUsuario (models.Model):
    name = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    password = models.TextField(max_length=50)


# Create your models here.
