from django.http import HttpResponse
from django.shortcuts import render
import importlib
person = importlib.import_module('person.models')
Victim = person.Victim



def index(request):
    victims = Victim.objects.all()
    context = {'victims': victims}
    return render(request, 'main.html', context)