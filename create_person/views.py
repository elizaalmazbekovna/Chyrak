from django.shortcuts import render, redirect
from .forms import PersonForm

def add_person(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PersonForm(request.POST, request.FILES)
            if form.is_valid():
                person = form.save(commit=False)
                person.user = request.user
                person.save()
                return redirect('list_of_person', pk=person.pk)
        else:
            form = PersonForm()
        return render(request, 'add_person.html', {'form': form})
    else:
        return redirect('/accounts/login/')

