from django.core.paginator import Paginator
from django.shortcuts import render
from person.models import Victim


def list_of_person(request):
    sort_option = request.GET.get('sort_option', 'first_name')
    items = Victim.objects.order_by(sort_option)

    if sort_option.startswith('-'):
        sort_option = sort_option[1:]  # Remove the hyphen
        items = sorted(items, key=lambda x: getattr(x, sort_option), reverse=True)
    else:
        items = sorted(items, key=lambda x: getattr(x, sort_option))

    paginator = Paginator(items, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        'items': items,
        'sort_option': sort_option,
    }
    return render(request, 'list_of_person.html', context)


