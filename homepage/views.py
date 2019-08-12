from django.shortcuts import render
from django.http import HttpResponse


test_data = [
    {
        'author': 'Derrezed',
        'title': 'Test1',
        'content': 'Test1',
        'date_posted': 'August 12, 2019'
    }
]

def homepage(request):
    context = {
        'posts': test_data
    }

    return render(request, 'homepage/home.html', context)


def about(request):
    return render(request, 'homepage/home.html')