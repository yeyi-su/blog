from django import forms

from .models import Persona

class PostForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'dni', 'direccion', 'fecha_de_nacimiento', 'fecha_de_alta')

