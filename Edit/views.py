
from create_person.forms import PersonForm
from django.shortcuts import render, redirect, get_object_or_404
from person.models import Victim


from django.utils.html import strip_tags

def edit_person(request, person_id):
    if request.user.is_authenticated:
        person = get_object_or_404(Victim, id=person_id, profile=request.user.profile)

        if request.method == 'POST':
            form = PersonForm(request.POST, request.FILES, instance=person)
            if form.is_valid():
                old_content = strip_tags(person.content)  # Get the previous content
                form.save()
                new_content = strip_tags(form.cleaned_data['content'])  # Get the updated content

                # Calculate the number of letters edited
                num_letters_edited = abs(len(old_content) - len(new_content))

                # Update the person object with the edited content and number of letters edited
                person.before_edit_content = old_content
                person.after_edit_content = new_content
                person.save()

                return redirect('person_page', person_id=person_id)
        else:
            form = PersonForm(instance=person)

        return render(request, 'edit_person.html', {'form': form})
    else:
        return redirect('/accounts/login/')




