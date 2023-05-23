from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from person.models import Victim

def search(request):
    query = request.GET.get('q')
    sort_option = request.GET.get('sort_option')

    results = None

    if query:
        search_filters = Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(content__icontains=query)
        results = Victim.objects.filter(search_filters)

        if sort_option:
            results = results.order_by(sort_option)

    paginator = Paginator(results, 7)
    page_number = request.GET.get("page")

    if results is not None:
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = None

    context = {
        "results": results,
        "page_obj": page_obj,
        "sort_option": sort_option,
        "q": query,
    }
    return render(request, 'search_page.html', context)
