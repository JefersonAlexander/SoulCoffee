from django import forms

class FormularioContacto(forms.Form):

 nombre= forms.CharField(label="Nombre", required=True)
 email= forms.CharField(label="Email", required=True)
 telefono=forms.CharField(label="Telefono", required=False)
 contenido=forms.CharField(label="Descripcion", required=True, widget=forms.Textarea)