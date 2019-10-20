from django.urls import path

from Space_FireFly.FireFly import views

urlpatterns = [
    path('', views.index, name='Inicio'),
]