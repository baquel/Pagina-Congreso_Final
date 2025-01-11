from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import UserRegisterForm, UserEditForm
from users.models import Avatar

# Create your views here.
def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            
            if user is not None:
                login(request, user)
                return render(request, "App_Pagina/inicio.html")
        
        msg_login = "Usuario o contraseña incorrectos"
    
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def registro(request):
    
    msg_registro = ""
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "App_Pagina/inicio.html")
    
        msg_registro = "Error en los datos ingresados"

    form = UserRegisterForm()
    return render(request, "users/registro.html", {"form": form, "msg_registro": msg_registro})

@login_required
def editar_perfil(request):
    usuario = request.user
    
    avatar, created = Avatar.objects.get_or_create(user=usuario)
    
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miFormulario.is_valid():
            
            if miFormulario.cleaned_data.get('image'):
                usuario.avatar.image = miFormulario.cleaned_data.get('image')
                usuario.avatar.save()
                
            miFormulario.save()
            return render(request, "App_Pagina/inicio.html")
    else:
        miFormulario = UserEditForm(instance=usuario)
        
    return render(request, "users/editar_perfil.html", {"mi_form": miFormulario})

class cambiar_contrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name='users/cambiar_contrasenia.html'
    success_url = reverse_lazy("EditarPerfil")