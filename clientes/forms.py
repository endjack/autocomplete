from ajax_select.fields import AutoCompleteSelectMultipleField
from django.forms import ModelForm, fields
from .models import *

class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

    endereco = AutoCompleteSelectMultipleField('endereco')