from django.shortcuts import render
from .models import Victim
def person_page(request):
    victims = Victim.objects.all()
    context = {'victims': victims}
    return render(request, 'about_person.html', context)