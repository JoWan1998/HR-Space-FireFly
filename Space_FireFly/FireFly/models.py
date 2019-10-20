
from django.db import models
#bd
# Create your models here.
from django.forms import ModelForm


class data(models.Model):
    file = models.FileField(upload_to="document/")






