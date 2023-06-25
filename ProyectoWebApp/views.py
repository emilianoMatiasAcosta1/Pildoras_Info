from django.shortcuts import render, HttpResponse


def home(resquest):
    return render(resquest, 'ProyectoWebApp/home.html')

def service(resquest):
    return render(resquest, 'ProyectoWebApp/service.html')

def store(resquest):
    return render(resquest, 'ProyectoWebApp/store.html')

def blog(resquest):
    return render(resquest, 'ProyectoWebApp/blog.html') 

def contact(resquest):
    return render(resquest, 'ProyectoWebApp/contact.html')


