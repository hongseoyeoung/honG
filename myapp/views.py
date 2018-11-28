from django.shortcuts import render
from django.utils import timezone
from .models import Lecture_note


# 회원가입을 하기위한 라이브러리

# from django.contrib.auth.forms import UserCreationForm
# from django.views import generic

from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CreateUserForm
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def lecture_note(request):
    lecture_lists = Lecture_note.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'lecture_note/lecture_note.html', {'lecture_lists': lecture_lists})


# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

class CreateUserView(CreateView): # generic view중에 CreateView를 상속받는다.
    template_name = 'registration/signup.html' # 템플릿은?
    form_class =  CreateUserForm # 푸슨 폼 사용? >> 내장 회원가입 폼을 커스터마지징 한 것을 사용하는 경우
    # form_class = UserCreationForm >> 내장 회원가입 폼 사용하는 경우
    success_url = reverse_lazy('create_user_done') # 성공하면 어디로?

class RegisteredView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'registration/signup_done.html' # 템플릿은?
