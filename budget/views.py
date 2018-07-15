from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Yabadabadoo")
# Create your views here.
