from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>i am very lasy fellow</h1>')

def second(request):
    return HttpResponse('<h1>i am daily wack up at 7</h1>')

