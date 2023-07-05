from django.forms import ModelForm
from . models import *

class FondateurForm(ModelForm):
    class Meta:
        model=Fondateur
        fields="__all__"

