from django.shortcuts import render
from django.utils import timezone
from .models import Lecture_note


# 회원가입을 하기위한 라이브러리

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic



# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def lecture_note(request):
    lecture_lists = Lecture_note.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'lecture_note/lecture_note.html', {'lecture_lists': lecture_lists})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'