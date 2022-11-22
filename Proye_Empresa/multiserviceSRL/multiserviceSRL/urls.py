"""multiserviceSRL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from multiserviceSRL.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vista-saludos/', vista_saludos),
    path('fecha/', dia_hoy),
    path("prueba_template/", probando_template),
    path("prueba2_de_template_pero_pasando_contexto_variables/", probando_template_metodo2),
    path("prueba3_de_template_listas_for_datetime/", probando_template_metodo3),
    path("prueba4_de_template_if_filtro_color_notas/",probando_template_metodo4),
    path("prueba5_de_template_muestro_lista_enumerada/",probando_template_metodo5),
    path("prueba6_incorporando_cargador_de_plantillas/",vista_usando_cargador_de_plantillas_loader),
]
