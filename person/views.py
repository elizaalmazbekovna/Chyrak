from django.shortcuts import render, get_object_or_404
from .models import Victim
def person_page(request, person_id):
    victim = Victim.objects.get(id=person_id)
    context = {
        'victim': victim,
        'person_id':person_id
    }

    return render(request, 'about_person.html', context)