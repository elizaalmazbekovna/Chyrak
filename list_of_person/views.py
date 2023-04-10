from django.core.paginator import Paginator
from django.shortcuts import render
from person.models import Victim


def list_of_person(request):
    victim_articles = Victim.objects.all().order_by('first_name').values()
    paginator = Paginator(victim_articles, 3)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    return render(request, 'list_of_person.html', context)