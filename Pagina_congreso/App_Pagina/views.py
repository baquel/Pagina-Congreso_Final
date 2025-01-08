from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from App_Pagina.forms import AutoresForm, BuscarForm
from App_Pagina.models import Autores, Resumenes, Revisores

def inicio(request):
    return render(request, "App_Pagina/inicio.html")

def autores(request):
    if request.method == "POST":
        
        mi_formulario = AutoresForm(request.POST)
        
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            
            informacion = mi_formulario.cleaned_data
            
            autores = Autores(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], codigo_postal=informacion['codigo_postal'])
            
            autores.save()
            
            resumenes = Resumenes(titulo=informacion['titulo'], cuerpo=informacion['cuerpo'], poster=informacion['poster'], fecha_revision=informacion['fecha_revision'])
            
            resumenes.save()
            
            revisores = Revisores(nombre=informacion['nombre_revisor'], apellido=informacion['apellido_revisor'], email=informacion['email_revisor'], area=informacion['area'])
            
            revisores.save()
            
            return render(request, "App_Pagina/inicio.html")
        
    else:
        mi_formulario=AutoresForm()
    
    return render(request, "App_Pagina/autores.html", {"mi_formulario":mi_formulario})
    
def buscar(request):
    
    if request.method == "POST":
        
        mi_formulario = BuscarForm(request.POST)
        
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
        
            resumenes = Resumenes.objects.filter(titulo__icontains=informacion["palabra_clave"])
        
            return render(request, "App_Pagina/resultados.html", {"resumenes": resumenes})
    
    else:
        mi_formulario = BuscarForm()
    
    return render(request, "App_Pagina/buscar.html", {"mi_formulario": mi_formulario}) 