from django.shortcuts import render
from .models import Servicio

def lista_servicios(request):
    servicios = Servicio.objects.all() # Aquí jalamos todo de la base de datos
    return render(request, 'index.html',{'servicios': servicios})

# Create your views here.
