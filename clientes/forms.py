from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelect
from django import forms
from .models import *

# class ClienteForm(forms.ModelForm):

#     class Meta:
#         model = Cliente
#         fields = '__all__'

#     endereco = AutoCompleteSelectMultipleField('endereco')
    
class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'endereco': AutocompleteSelect(
             Endereço._meta.get_field('rua').remote_field,
            admin.site,
         )
         }