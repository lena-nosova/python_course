from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.

def get_random(request):
    return(HttpResponse("<h2>Result</h2>" + str(randint(0, 100000))))
    

