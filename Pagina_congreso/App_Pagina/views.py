from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from App_Pagina.forms import ResumenesForm, BuscarForm
from App_Pagina.models import Autores, Resumenes, Revisores

def inicio(request):
    return render(request, "App_Pagina/inicio.html")

def about(request):
    return render(request, "App_Pagina/about.html")

@login_required
def crear_resumen(request):
    if request.method == "POST":
        
        mi_formulario = ResumenesForm(request.POST)
        
        print(mi_formulario)
        
        if mi_formulario.is_valid():
            
            informacion = mi_formulario.cleaned_data
                                  
            autores = Autores(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], codigo_postal=informacion['codigo_postal'])
            
            autores.save()
            
            resumenes = Resumenes(titulo=informacion['titulo'], cuerpo=informacion['cuerpo'], poster=informacion['poster'], fecha_revision=informacion['fecha_revision'])
            
            resumenes.save()
                                 
            revisores = Revisores(nombre=informacion['nombre_revisor'], apellido=informacion['apellido_revisor'], email=informacion['email_revisor'], area=informacion['area'])
            
            revisores.save()                      
            
            return render(request, "App_Pagina/inicio.html")
        
    else:
        mi_formulario=ResumenesForm()
    
    return render(request, "App_Pagina/crear_resumen.html", {"mi_formulario":mi_formulario})

def buscar(request):
    
    if request.method == "POST":
        
        mi_formulario = BuscarForm(request.POST)
        
        print(mi_formulario)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
        
            resumenes = Resumenes.objects.filter(titulo__icontains=informacion["palabra_clave"])
        
            return render(request, "App_Pagina/resultados.html", {"resumenes": resumenes})
    
    else:
        mi_formulario = BuscarForm()
    
    return render(request, "App_Pagina/buscar.html", {"mi_formulario": mi_formulario}) 

class ResumenesListView(ListView):
    model = Resumenes
    context_object_name = "resumenes"
    template_name = "App_Pagina/resultados.html"

class ResumenesDetailView(DetailView):
    model = Resumenes    
    template_name = "App_Pagina/resultados_detalle.html"

class ResumenesDeleteView(LoginRequiredMixin, DeleteView):
    model = Resumenes
    template_name = "App_Pagina/eliminar_resumen.html"
    success_url = reverse_lazy('ListarResumen')
    
    def post(self, request, *args, **kwargs):
        if request.user.is_staff:
            super().post(request, *args, **kwargs)
        return render(request, "App_Pagina/inicio.html")

class ResumenesUpdateView(LoginRequiredMixin, UpdateView):
    model = Resumenes
    template_name = "App_Pagina/editar_resumen.html"
    success_url = reverse_lazy('ListarResumen')    
    fields = ['titulo', 'cuerpo', 'poster']