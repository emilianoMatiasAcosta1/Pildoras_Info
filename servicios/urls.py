from django.urls import path
from servicios.views import service
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('service/', service, name='service'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 