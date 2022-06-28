from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'movie/home.html')



def result(request):
    return HttpResponse('<h1>hello world 2</h1>')