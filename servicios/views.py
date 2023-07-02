from django.shortcuts import render
from servicios.models import Servicio

def service(request):
    traer = Servicio.objects.all()
    context = {'servicio_la_corunia' : traer}
    return render(request, 'servicios/service.html', context)             # CONTEXTO _ nombre que usaremos en el template 
