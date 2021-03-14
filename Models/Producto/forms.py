from django import forms
from Models.Producto.models import Producto



class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {'descripcion': forms.Textarea(attrs={'type': 'textarea','rows': '5'})}





