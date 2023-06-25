from django.db import models

class Servicio(models.Model):
    titulo= models.CharField(max_length=50) 
    contenido= models.CharField(max_length=50) 
    imagen= models.ImageField(blank=True, upload_to='Servicio')
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now_add=True)                    
 
    class Meta:                                                  # class Meta -->  Algunas configuraciones de nuestro modelo
        verbose_name= 'servicios La Coruña'                       # verbose_name  -->  En este caso te cambia como figura el nombre el el admin
      

    def __str__(self):
        return (f'{self.titulo}')    


