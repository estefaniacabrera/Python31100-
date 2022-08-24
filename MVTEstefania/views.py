from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Familiares


def familia(request):
    familiar1 = Familiares(nombre="Marcos", edad=30, fechaNacimiento="1992-10-10")
    familiar2 = Familiares(nombre="Juana", edad=40, fechaNacimiento="1982-11-15")
    familiar3 = Familiares(nombre="Maria", edad=65, fechaNacimiento="1957-03-09")
    familiar1.save()
    familiar2.save()
    familiar3.save()
    texto = {
        "nombre": familiar1.nombre,
        "edad": familiar1.edad,
        "nacimiento": familiar1.fechaNacimiento,
        "nombre2": familiar2.nombre,
        "edad2": familiar2.edad,
        "nacimiento2": familiar2.fechaNacimiento,
        "nombre3": familiar3.nombre,
        "edad3": familiar3.edad,
        "nacimiento3": familiar3.fechaNacimiento,
    }
    plantilla = loader.get_template("template2.html")
    documento = plantilla.render(texto)
    return HttpResponse(documento)