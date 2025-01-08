
from django.urls import path
from App_Pagina import views

urlpatterns = [
    path('', views.inicio, name="Inicio")    
       
]

forms_api = [
    path('autores/', views.autores, name="Autores"),
    path('buscar', views.buscar, name="Buscar")
]

urlpatterns += forms_api