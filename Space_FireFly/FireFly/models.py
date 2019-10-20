from csvImporter.model import CsvModel
from django.db import models
#bd
# Create your models here.
class data(models.Model):
    nombre = models.CharField()
    file = models.FileField()

    def __str__(self):
        return self.nombre



