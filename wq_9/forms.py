from django import forms
from . import models



class RegForm(forms.ModelForm):
    class Meta():
        models = models.Registration
        fields = ('Name','Email','Phone','Qualification','Interested Course','Message')
        