
from django.urls import path
from App_Pagina import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about', views.about, name="About")    
       
]

forms_api = [
    path('crear_resumen/', views.crear_resumen, name="CrearResumen"),
    path('buscar/', views.buscar, name="Buscar"),
    path('listar_resumenes/', views.ResumenesListView.as_view(), name="ListarResumen"),
    path('ver_resumen/<pk>', views.ResumenesDetailView.as_view(), name="VerResumen"),
    path('editar_resumen/<pk>/', views.ResumenesUpdateView.as_view(), name="EditarResumen"),
    path('borrar_resumen/<pk>/', views.ResumenesDeleteView.as_view(), name="BorrarResumen")    
]

urlpatterns += forms_api