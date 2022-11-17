from django.http import HttpRequest, HttpResponse
from django.template import Template, Context

def temp(request):
    
    nom="Nahuel"
    ap="Agnese"
    diccionario={"nombre":nom, "apellido":ap}
    
    archivo=open("entregable1\Templates\index.html")
    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccionario)

    documento=template.render(contexto)
    return HttpResponse(documento)