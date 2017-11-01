from django.shortcuts import render
from core.templates import *

def home(request):
    return render(request, "index.html")