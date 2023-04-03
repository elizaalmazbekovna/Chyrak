from django.shortcuts import render
from person.models import Victim, Article


def list_of_person(request):
    victims = Victim.objects.filter()
    victim_articles = Article.objects.all()
    context = {"victims": victims, victim_articles: victim_articles}
    return render(request, 'list_of_person.html', context)
