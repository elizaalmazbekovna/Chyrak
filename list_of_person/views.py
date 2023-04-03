from django.shortcuts import render
from person.models import Victim, Article


def list_of_person(request):
    victim = Victim.objects.all()
    victim_article = Article.objects.all()
    context = {"victim": victim, "victim_article": victim_article}
    return render(request, 'list_of_person.html', context)
