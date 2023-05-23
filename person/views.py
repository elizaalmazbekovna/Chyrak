import datetime
import locale
from django.shortcuts import render, get_object_or_404
from .models import Victim

def person_page(request, person_id):
    victim = get_object_or_404(Victim, id=person_id)

    month_names_kyrgyz = {
        1: 'Үчтүн айы',
        2: 'Бирдин айы',
        3: 'Жалган Куран',
        4: 'Чын Куран',
        5: 'Бугу',
        6: 'Кулжа',
        7: 'Теке',
        8: 'Баш Оона',
        9: 'Аяк Оона',
        10: 'Тогуздун айы',
        11: 'Жетинин айы',
        12: 'Бештин айы'
    }


    birth_date = "{day}-{month}, {year}-жыл".format(
        day = victim.date_of_birth.day,
        month = month_names_kyrgyz[victim.date_of_birth.month],
        year = victim.date_of_birth.year
    )

    death_date = "{day}-{month}, {year}-жыл".format(
        day = victim.date_of_death.day,
        month = month_names_kyrgyz[victim.date_of_death.month],
        year = victim.date_of_death.year
    )

    paragraphs = []
    sentences = victim.content.split('. ')
    current_paragraph = []
    for i, sentence in enumerate(sentences):
        if i < len(sentences) - 1:
            current_paragraph.append(sentence + '. ')
        else:
            current_paragraph.append(sentence)
        if len(current_paragraph) == 5:
            paragraphs.append(current_paragraph)
            current_paragraph = []

    if current_paragraph:
        paragraphs.append(current_paragraph)


    if victim.rehabilitated:
        reh = 'Акталган'
    else:
        reh = 'Акталбай калган'


    context = {
        'victim': victim,
        'person_id': person_id,
        'birth_date': birth_date,
        'death_date': death_date,
        'reh': reh,
        'paragraphs': paragraphs,

    }

    return render(request, 'about_person.html', context)



def edit_history(request, person_id):
    victim = get_object_or_404(Victim, id=person_id)

    # Fetch the editing history for the person
    editing_history = victim.editinghistory_set.order_by('-date_of_editing')

    context = {
        'victim': victim,
        'editing_history': editing_history,
    }

    return render(request, 'edit_history.html', context)
