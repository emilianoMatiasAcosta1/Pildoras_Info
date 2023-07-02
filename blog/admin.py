from django.contrib import admin
from blog.models import Blog, Categoria 

class BlogAdmin(admin.ModelAdmin):
    list_display = ['titulo','descripcion']
    readonly_fields = ['creado','actualizado']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']    
    readonly_fields = ['creado','actualizado']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Categoria, CategoriaAdmin)