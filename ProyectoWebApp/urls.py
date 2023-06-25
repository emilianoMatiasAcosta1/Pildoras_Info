from django.urls import path
from ProyectoWebApp.views import home, service, store, blog, contact
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('service/', service, name='service'),
    path('store/', store, name='store'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 