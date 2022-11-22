from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime


def vista_saludos(request):
    hoy= datetime.now().strftime("%d|%m|%Y")
    respuesta= (f"Hoy es {hoy}     Bienvenido estimado cliente:")
    return HttpResponse(respuesta)
    
def dia_hoy(request):
    hoy=datetime.now()
    return HttpResponse(f"Fecha / Horario actual: {hoy}")


    
    


def inicio(request):
    pass
