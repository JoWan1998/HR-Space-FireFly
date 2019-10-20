
from django.db import models
#bd
# Create your models here.
class data(models.Model):
    nombre = models.CharField(max_length=100)
    file = models.FileField(upload_to="../archivos/", null=True, blank=True)

    def __str__(self):
        return self.nombre



