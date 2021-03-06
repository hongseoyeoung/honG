from django.shortcuts import render
from django.utils import timezone
from .models import Lecture_note
from django.shortcuts import redirect
# 회원가입을 하기위한 라이브러리

# from django.contrib.auth.forms import UserCreationForm
# from django.views import generic

from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CreateUserForm,Lecture_noteForm
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404
from django.db import models


# Create your views here.
def contact(request):
    if request.method == "POST":
        email = EmailMessage(request.POST['name']+'의 메일',request.POST['phone'] +request.POST['message'] ,request.POST['email'], to=['khbasd@gmail.com'])
        email.send()

    return render(request, 'home/contact.html',{})



def index(request):
    return render(request, 'home/index.html')

def lecture_note(request):
    lecture_lists = Lecture_note.objects.filter(created_date__lte=timezone.now()).order_by('created_date').reverse()
    return render(request, 'lecture_note/lecture_note.html', {'lecture_lists': lecture_lists})

def lecture_detail(request, pk):
    lecture = get_object_or_404(Lecture_note, pk=pk)
    return render(request, 'lecture_note/lecture_detail.html', {'lecture': lecture})


def lecture_new(request):
    if request.method == "POST":
        form = Lecture_noteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('lecture_detail', pk=post.pk)
    else:
        form = Lecture_noteForm()
    return render(request, 'lecture_note/new.html', {'form': form})


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
