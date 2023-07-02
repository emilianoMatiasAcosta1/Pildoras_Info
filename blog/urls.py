from django.urls import path
from blog.views import blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blog/', blog, name='blogg'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)