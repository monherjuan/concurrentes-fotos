from django.db import models

# Create your models here.
class fotoModel(models.Model):
    url = models.ImageField()