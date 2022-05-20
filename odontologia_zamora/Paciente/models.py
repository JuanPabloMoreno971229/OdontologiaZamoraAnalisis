from django.db import models

# Create your models here.



class paciente(models.Model):

    Id_paciente = models.AutoField(primary_key=True, verbose_name="Id")
    name = models.CharField(max_length=200, null=False, verbose_name="Nombre")
    email = models.CharField(max_length=200, null=False, verbose_name="Correo")
    phone = models.CharField(max_length=200, null=False, verbose_name="Telefono")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
                
    def __str__(self):
        return self.name    