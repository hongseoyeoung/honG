from django.shortcuts import render
import urllib.request
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    return render(request,'home/index.html')

def basic_grid(request):
    return render(request,'home/basic-grid.html')

def full_width(request):
    return render(request,'home/full-width.html')

def gallery(request):
    return render(request,'home/gallery.html')

def sidebar_left(request):
    return render(request,'home/sidebar-left.html')

def sidebar_right(request):
    return render(request,'home/sidebar-right.html')
