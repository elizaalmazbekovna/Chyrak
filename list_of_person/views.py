from django.core.paginator import Paginator
from django.shortcuts import render
from person.models import Victim

def list_of_person(request):
    sort_option = request.GET.get('sort_option', 'first_name')
    all_items = Victim.objects.all().order_by(sort_option)

    paginator = Paginator(all_items, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        'items': page_obj.object_list,
        'sort_option': sort_option,
    }
    return render(request, 'list_of_person.html', context)
