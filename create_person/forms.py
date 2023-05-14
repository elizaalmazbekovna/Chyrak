from django import forms
from person.models import Victim


from django.forms.widgets import SelectDateWidget
class PersonForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget())
    date_of_death = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Victim
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'place_of_birth', 'place_of_death', 'nationality',
                  'blame', 'rehabilitated', 'occupation', 'bedfellow', 'children', 'photo', 'desc_of_photo', 'file', 'desc_of_file', 'content']