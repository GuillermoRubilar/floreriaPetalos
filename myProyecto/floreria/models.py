from django.db import models

# Create your models here.
class Categoria(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    calificacion=models.IntegerField()

    def __str__(self):
        return self.name

class Flor(models.Model):
    name=models.CharField(max_length=100, primary_key=True)
    estado=models.TextField()
    valor=models.IntegerField()
    descripcion=models.TextField()
    stock=models.IntegerField()
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    fotografia=models.ImageField(upload_to="floor",null=True)

    def __str__(self):
        return self.name
