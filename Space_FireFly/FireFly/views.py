from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
from .forms import FormEntrada
from .models import data



def index(request):
    return HttpResponse("NASA, primer vistazo a SPACE FIREFLY")


def entrada(request):
    if request.method == 'POST':
        form = FormEntrada(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            archivo = request.FILES['archivo']

            insert = data(nombre=titulo, file=archivo)
            insert.save()

            return HttpResponseRedirect('success')
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return HttpResponseRedirect('error')
