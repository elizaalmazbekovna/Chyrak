from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import PersonForm


# @login_required(login_url='/accounts/login/')
def add_person(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PersonForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('list_of_person')
        else:
            form = PersonForm()

        return render(request, 'add_person.html', {'form': form})
    else:
        return redirect('/accounts/login/')
