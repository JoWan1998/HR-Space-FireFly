from django.urls import path

from . import views

urlpatterns = [
    path('Inicio/', views.index, name='Inicio'),
    path('Upload/',views.entrada, name='Upload'),
]