from django.conf.urls import url
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='Inicio'),
    url(r'^Equipo/$',views.equipo, name='Equipo'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)