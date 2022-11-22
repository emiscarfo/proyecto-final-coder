from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime


def vista_saludos(request):
    hoy= datetime.now().strftime("%d/%m/%Y")
    respuesta= (f"Hoy es {hoy}     Bienvenido estimado cliente:")
    return HttpResponse(respuesta)
    
def dia_hoy(request):
    hoy=datetime.now().strftime("%d/%m/%Y / son las %H : %M hs")
    return HttpResponse(f"Fecha / Horario actual: {hoy}")

def probando_template(self):
    mihtml= open(r"C:\Users\GAMER DELL\visual estudio EMI\DJANGO\Proye_Empresa\multiserviceSRL\multiserviceSRL\templates\plantilla1.html")
    plantilla= Template(mihtml.read())
    mihtml.close()
    micontexto= Context()
    documento= plantilla.render(micontexto)
    return HttpResponse(documento)

def probando_template_metodo2(self):
    nom= "Emiliano"
    ap= "Scarfo"
    diccionario= {"Nombre":nom, "Apellido":ap}
    mihtml= open(r"C:\Users\GAMER DELL\visual estudio EMI\DJANGO\Proye_Empresa\multiserviceSRL\multiserviceSRL\templates\plantilla2.html")
    plantilla= Template(mihtml.read())
    mihtml.close()
    micontexto= Context(diccionario)
    documento= plantilla.render(micontexto)
    return HttpResponse(documento)

def probando_template_metodo3(self):
    nom= "Emiliano"
    ap= "Scarfo"
    lista_notas= [8,7,9,10,8,9]
    diccionario= {"Nombre":nom, "Apellido":ap, "hoy":datetime.now().strftime("%d/%m/%Y"),"notas":lista_notas}
    mihtml= open(r"C:\Users\GAMER DELL\visual estudio EMI\DJANGO\Proye_Empresa\multiserviceSRL\multiserviceSRL\templates\plantilla3.html")
    plantilla= Template(mihtml.read())
    mihtml.close()
    micontexto= Context(diccionario)
    documento= plantilla.render(micontexto)
    return HttpResponse(documento)
    pass

def probando_template_metodo4(self):
    nom= "Emiliano"
    ap= "Scarfo"
    lista_notas= [8,1,7,3,10,2,8,9]
    diccionario= {"Nombre":nom, "Apellido":ap, "hoy":datetime.now().strftime("%d/%m/%Y"),"notas":lista_notas}
    mihtml= open(r"C:\Users\GAMER DELL\visual estudio EMI\DJANGO\Proye_Empresa\multiserviceSRL\multiserviceSRL\templates\plantilla4.html")
    plantilla= Template(mihtml.read())
    mihtml.close()
    micontexto= Context(diccionario)
    documento= plantilla.render(micontexto)
    return HttpResponse(documento)

def probando_template_metodo5(self):
  
    mihtml= open(r"C:\Users\GAMER DELL\visual estudio EMI\DJANGO\Proye_Empresa\multiserviceSRL\multiserviceSRL\templates\plantilla5.html")
    plantilla= Template(mihtml.read())
    mihtml.close()
    listado_alumnos = ["Emiliano Scarfo","Laura Gonzalez", "Eva Araujo", "Matias Scarfo", "Sofia Asen Scarfo", "Susana Lewkow"]
    datos= {"tecnologia":"Cobol","lista_alumnos":listado_alumnos}
    contexto= Context(datos)
    documento= plantilla.render(contexto)
    return HttpResponse(documento)

def vista_usando_cargador_de_plantillas_loader(request):
    # Creamos el diccionario de datos
    listado_alumnos = ["Emiliano Scarfo","Laura Gonzalez", "Eva Araujo", "Matias Scarfo", "Sofia Asen Scarfo", "Susana Lewkow"]
    datos= {"tecnologia":"Cobol","lista_alumnos":listado_alumnos}
    plantilla= loader.get_template("plantilla5.html")
    documento= plantilla.render(datos)
    return HttpResponse(documento)

    pass

def inicio(request):
    pass
