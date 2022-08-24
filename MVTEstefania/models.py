from django.db import models


class Familiares(models.Model):

    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField()
