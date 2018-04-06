from django.shortcuts import render
from . import models
from . import forms
# Create your views here.

from django.views import generic

class RegistrationCreate(generic.CreateView):
    model = models.Registration
    form_class = forms.RegForm
    template_name = 'registration_form.html'


class Home(generic.TemplateView):
    template_name = 'home_page.html'

class Contact(generic.TemplateView):
    template_name = 'contactus.html'

class Course1(generic.TemplateView):
    template_name = 'courses/webdesigning.html'

class Course2(generic.TemplateView):
    template_name = 'courses/phptraining.html'

class Course3(generic.TemplateView):
    template_name = 'courses/javatraining.html'

class Course4(generic.TemplateView):
    template_name = 'courses/androidtraining.html'



