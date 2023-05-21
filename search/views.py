from django.core.paginator import Paginator
from django.shortcuts import render
from person.models import Victim

def search(request):
    query = request.GET.get('q')
    results = None
    paginator = Paginator([], 2)

    if query:
        results = Victim.objects.filter(content__icontains=query)
        paginator = Paginator(results, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "results": results,
    }
    return render(request, 'search_page.html', context)
