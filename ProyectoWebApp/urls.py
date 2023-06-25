from django.urls import path
from ProyectoWebApp.views import home, service, store, blog, contact


urlpatterns = [
    path('', home, name='home'),
    path('service/', service, name='service'),
    path('store/', store, name='store'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact')
]