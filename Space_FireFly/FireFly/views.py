from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
from .forms import FormEntrada
from .models import data




def index(request):
    if request.method == 'POST':
        form = FormEntrada(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            archivo = request.FILES['archivo']

            insert = data(nombre=titulo, file=archivo)
            insert.save()

            return render(request,'index.html',context={'mensaje':'EXITO'})
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        form = FormEntrada()
        return render(request,'index.html',context={'mensaje':'Ingresa el archivo!!'})

def equipo(request):
    return render(request,'contact.html',context={})


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
