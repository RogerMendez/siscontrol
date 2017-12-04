from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Login_view, name="ingresar"),
    url(r'^inicio/$', Inicio, name="inicio"),
    url(r'^ayuda/$', Ayuda, name="ayuda"),
    url(r'^salir/$', Logout_view, name="salir"),

]