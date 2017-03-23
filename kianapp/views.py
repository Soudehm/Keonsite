from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def hello(request):
#   text = """<h1>welcome to my app !</h1>"""
#   return HttpResponse(text)


def welcome(request):
    return render(request, 'kianapp/welcome.html', {})


def news(request):
    return render(request, 'kianapp/news.html', {})
