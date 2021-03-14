from django import forms
from django.forms import ModelForm,DateInput
from Models.Categoria.models import Categoria


class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


