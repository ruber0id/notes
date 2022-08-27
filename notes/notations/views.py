from django.shortcuts import render
from .models import Notes


def notes_home(request):
    notes = Notes.objects.order_by('-date_added')
    return render(request, 'notations/notes_home.html', {'notes': notes})
