from django import forms
from . import models



class RegForm(forms.ModelForm):
    class Meta():
        model = models.Registration
        fields = ('Name','Email','Phone','Qualification','InterestedCourse')
        