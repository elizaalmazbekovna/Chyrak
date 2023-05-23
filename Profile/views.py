
from person.models import Victim
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile


def create_profiles():
    users = User.objects.all()

    for user in users:
        if not Profile.objects.filter(user=user).exists():
            Profile.objects.create(user=user)

create_profiles()


@login_required
def profile_page(request):
    profile = get_object_or_404(Profile, user=request.user)
    victims = Victim.objects.filter(profile=profile)

    context = {
        'profile': profile,
        'victims': victims
    }
    return render(request, 'profile.html', context)




