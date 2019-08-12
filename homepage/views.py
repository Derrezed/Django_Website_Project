from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse('<h1>Test1</h1>')


def about(request):
    return HttpResponse('<h1>Test2</h1>')