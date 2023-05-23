from django.shortcuts import render
from django.shortcuts import render, redirect
from create_person.forms import PersonForm
from django.shortcuts import render, redirect, get_object_or_404
from person.models import Victim

# Create your views here.
#
# def edit_person(request, person_id):
#     victim = get_object_or_404(Victim, id=person_id)
#
#     if request.user != victim.profile.user:
#         return redirect('person_page', person_id=victim.pk)
#
#     if request.method == 'POST':
#         form = PersonForm(request.POST, request.FILES, instance=victim)
#         if form.is_valid():
#             victim = form.save()
#             return redirect('person_page', person_id=victim.pk)
#     else:
#         form = PersonForm(instance=victim)
#
#     context = {
#         'form': form,
#         'person_id': person_id
#     }
#     return render(request, 'edit_person.html', context)

def edit_person(request, person_id):
    if request.user.is_authenticated:
        person = get_object_or_404(Victim or None, id=person_id, profile=request.user.profile)

        if request.method == 'POST':
            form = PersonForm(request.POST or None, request.FILES, instance=person)
            if form.is_valid():
                form.save()
                return redirect('person_page', person_id=person_id)
        else:
            form = PersonForm(instance=person)

        return render(request, 'edit_person.html', {'form': form})
    else:
        return redirect('/accounts/login/')




