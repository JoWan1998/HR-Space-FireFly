from xml.dom.minidom import Document

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
# Create your views here.
from django.template import RequestContext
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import dataForm
from .models import data

@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = dataForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = data(file = request.FILES['file'])
            if newdoc != None:
                print(newdoc.file.name)
                newdoc.save()
                messages.info(request,"exito")

            return HttpResponseRedirect(reverse(index))
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        form = dataForm()
        return render_to_response('index.html',{'mensaje':'','form':form},RequestContext(request))

def equipo(request):
    return render(request,'contact.html',context={})

