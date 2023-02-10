from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'title': 'Beautiful is better than ugly',
        'author': 'John Doe',
        'content': 'Beautiful is better than ugly',
        'published_at': 'October 1, 2022'
    },
    {
        'title': 'Explicit is better than implicit',
        'author': 'Jane Doe',
        'content': 'Explicit is better than implicit',
        'published_at': 'October 1, 2022'
    }
]


def index(request):
    context = {
        'posts' : posts,
        'title': 'Zen of Python'
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')
