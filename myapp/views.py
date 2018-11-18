from django.shortcuts import render
from django.utils import timezone
from .models import Lecture_note
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def lecture_note(request):
    lecture_lists = Lecture_note.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'lecture_note/lecture_note.html', {'lecture_lists': lecture_lists})