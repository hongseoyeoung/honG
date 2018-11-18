from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def lecture_note(request):
    return render(request, 'lecture_note/lecture_note.html')