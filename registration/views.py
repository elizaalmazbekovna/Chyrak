from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from registration.forms import CustomUserCreationForm


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()


            return redirect('/accounts/login/')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)