from django.shortcuts import render
from .models import Post


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
        'posts': Post.objects.all()
    }

    return render(request, 'homepage/home.html', context)


def about(request):
    return render(request, 'homepage/home.html')