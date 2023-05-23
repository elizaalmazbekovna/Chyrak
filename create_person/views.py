from django.shortcuts import render, redirect
from .forms import PersonForm
from django.shortcuts import render, redirect, get_object_or_404
from person.models import Victim



def add_person(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PersonForm(request.POST, request.FILES)
            if form.is_valid():
                victim = form.save(commit=False)
                victim.photo = form.cleaned_data['photo']

                # Get the profile associated with the authenticated user
                profile = request.user.profile
                victim.profile = profile

                victim.save()
                return redirect('person_page', person_id=victim.pk)
        else:
            print("Kata")
            form = PersonForm()
        return render(request, 'add_person.html', {'form': form})
    else:
        return redirect('/accounts/login/')










