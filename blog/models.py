from django.db import models
from django.contrib.auth.models import User




class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return (f'{self.nombre}')    



class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='Blog', blank=True)    
    autor = models.ForeignKey(User , on_delete=models.CASCADE)                  # Asignamos el post al usuario - Luego si un usuario es borrado, junto a el se borran todos sus post 
    categoria = models.ManyToManyField(Categoria)                               # Establecemos una relacion con el modelo Categoria 
    creado = models.DateTimeField(auto_now_add=True)
    actualizado =  models.DateTimeField(auto_now_add=True)
                                                                                            
    class Meta:
        verbose_name = 'Blog La Coruña'
        verbose_name_plural = 'Blogs La Coruña'                                 # En el caso que django utilize por defecto plural, usara este nombre que le indicamos 
        
    def __str__(self):
        return(f'{self.titulo}')
       