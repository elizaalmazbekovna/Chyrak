from django.shortcuts import render
from person.models import Victim


def list_of_person(request):
    victim_articles = Victim.objects.all()
    context = {"victim_articles": victim_articles}
    return render(request, 'list_of_person.html', context)