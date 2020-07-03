from django.db import models

# Create your models here.

class Movie(models.Model): #SIEMPRE HAY QUE HEREDAR DE MODELS.MODEL
    title = models.CharField(max_length=140) #PARA PONER UN LIMITE DE LETRAS
    sinopsis = models.TextField(blank=True, null=True) #PARA PONER UN TEXTO SIN LONGITUD, lo de adentro del parentesis es cuando un dato no es totalmente necesario
    duration = models.PositiveIntegerField() #POSITIVE PARA CUANDO SOLO PUEDE SER UN NUMERO ENTERO POSITIVO
    calif = models.PositiveIntegerField(default=5) #Estamos especificndo por default lo del parentesis
    gender = models.CharField(max_length=50) 
    created = models.DateTimeField(auto_now_add=True) #PARA SABER CUANDO SE CREO LA PELICULA EN LA BASI DE DATOS
    updated = models.DateTimeField(auto_now=True) #PARA SABER CUANDO SE MODIFICO ESTA PELICULA EN LA BASE DE DATOS

    def __str__(self):
        return self.title

#CREAR UN MODELO PARA UN ACTOR

class Actor(models.Model):
    name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=225)
    experience_years = models.PositiveIntegerField()
    awards = models.PositiveIntegerField()
    biography = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True) #PARA SABER CUANDO SE CREO LA PELICULA EN LA BASI DE DATOS
    updated = models.DateTimeField(auto_now=True) #PARA SABER CUANDO SE MODIFICO ESTA PELICULA EN LA BASE DE DATOS

    def __str__(self):
        return self.name + ' ' + self.last_name