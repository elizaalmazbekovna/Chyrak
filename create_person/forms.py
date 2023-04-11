from django import forms
from person.models import Victim

class PersonForm(forms.ModelForm):
    class Meta:
        model = Victim
        fields = ['first_name', 'last_name','date_of_birth','date_of_death', 'place_of_birth','place_of_death','blame','rehabilitated','occupation','bedfellow','children','photo','content','is_proven']