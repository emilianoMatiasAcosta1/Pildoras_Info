from django.shortcuts import render, HttpResponse
from servicios.models import Servicio


def home(resquest):
    return render(resquest, 'ProyectoWebApp/home.html')


def store(resquest):
    return render(resquest, 'ProyectoWebApp/store.html')


def contact(resquest):  
    return render(resquest, 'ProyectoWebApp/contact.html')


