from django import forms
from .models import Junny

class JunnyForm(forms.ModelForm):
    class Meta:
        model = Junny
        fields = "__all__"