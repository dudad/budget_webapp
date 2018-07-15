from django.shortcuts import render
from django.http import HttpResponse
from .models import Outcome

def index(request):

    outcomes = Outcome.objects.all()[:10]
    context = {
        'outcomes' : outcomes
    }
    return render(request, 'budget/index.html', context)

def details(request, id):
    outcome = Outcome.objects.get(id=id)
    context = {
        'outcome' : outcome
    }

    return render(request, 'budget/details.html', context)
# Create your views here.
