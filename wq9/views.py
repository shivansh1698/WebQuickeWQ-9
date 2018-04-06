from django.shortcuts import render
from . import models
# Create your views here.

from django.views import generic

class RegistrationCreate(generic.CreateView):
    model = models.Registration
    