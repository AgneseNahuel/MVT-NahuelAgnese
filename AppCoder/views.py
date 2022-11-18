from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def familia(request):

    familia1=Familia(nombre="Nahuel", DNI=40781317, fechadecumpleaños="1997-10-25")
    familia2=Familia(nombre="Carolina", DNI=40781317, fechadecumpleaños="1997-10-25")
    familia3=Familia(nombre="Nacho", DNI=40781317, fechadecumpleaños="1997-10-25")
    familia1.save()
    familia2.save()
    familia3.save()
    cadena_texto="familia guardada "+familia1.nombre+" "+str(familia1.DNI)+" "+familia1.fechadecumpleaños
    cadena_texto2="familia guardada "+familia2.nombre+" "+str(familia2.DNI)+" "+familia2.fechadecumpleaños
    cadena_texto3="familia guardada "+familia3.nombre+" "+str(familia3.DNI)+" "+familia3.fechadecumpleaños
    return HttpResponse(cadena_texto+" "+cadena_texto2+" "+cadena_texto3)

#nueva manera de usar templates
def templateapp(request):
    return render(request, "AppCoder/indexapp.html",{"nombre":"Nahuel Agnese"})

def inicio(request):
    return render(request, "AppCoder/inicio.html")
