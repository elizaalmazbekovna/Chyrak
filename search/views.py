from django.shortcuts import render
from person.models import Victim

def search(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = Victim.objects.filter(content__icontains=query)
    return render(request, 'search_page.html', {'results': results})