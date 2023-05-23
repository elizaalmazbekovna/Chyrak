
from django.shortcuts import render, redirect, get_object_or_404
from person.models import Victim

# Create your views here.
def delete_person(request, person_id):
    person = get_object_or_404(Victim, pk=person_id)
    if request.method == 'POST':
        person.delete()
        return redirect('profile_page')

    return render(request, 'delete_person.html', {'person': person})