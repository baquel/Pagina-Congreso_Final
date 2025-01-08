from django import forms

class AutoresForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    codigo_postal = forms.IntegerField()
    titulo=forms.CharField()
    cuerpo=forms.CharField()
    poster=forms.BooleanField(required=False)    
    fecha_revision=forms.DateField()
    nombre_revisor=forms.CharField()
    apellido_revisor=forms.CharField()
    email_revisor=forms.CharField()
    area=forms.CharField()

class BuscarForm(forms.Form):
    palabra_clave = forms.CharField()