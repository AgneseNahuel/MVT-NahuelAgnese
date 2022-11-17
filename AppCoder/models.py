from django.db import models

# Create your models here.

#tabla y datos para bd
class Familia(models.Model):
    
    nombre=models.CharField(max_length=50)
    DNI=models.IntegerField()
    fechadecumpleaños=models.DateField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.DNI+" "+self.fechadecumpleaños