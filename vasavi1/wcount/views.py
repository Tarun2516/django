from django.shortcuts import render
import operator
from django.http import HttpResponse
def home(requests):
    return HttpResponse('<h1>Hello World<h1>')
def aboutus(requests):
    return HttpResponse('<h1>Hey Everyone<h1>')
def hobbies(requests):
    return HttpResponse('<h1>I like to read books,Sketching and doodling<h1>')
# Create your views here.
