from django.shortcuts import render, redirect, get_object_or_404
from create_person.forms import PersonForm
from person.models import Victim, EditingHistory

def edit_person(request, person_id):
    if request.user.is_authenticated:
        person = get_object_or_404(Victim, id=person_id, profile=request.user.profile)

        if request.method == 'POST':
            form = PersonForm(request.POST, request.FILES, instance=person)
            if form.is_valid():
                before_edit_content = person.content
                person = form.save()
                after_edit_content = person.content

                # Create a new EditingHistory entry
                editing_history = EditingHistory(
                    edited_by=request.user,  # Assign the User instance
                    before_edit_content=before_edit_content,
                    after_edit_content=after_edit_content,
                    victim=person
                )
                editing_history.save()

                return redirect('person_page', person_id=person_id)
        else:
            form = PersonForm(instance=person)

        return render(request, 'edit_person.html', {'form': form})
    else:
        return redirect('/accounts/login/')




