from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'HMK',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

# Handle traffic from homepage
# Return what the user should see
def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def myweb(request):
    return render(request, 'blog/myweb.html', {'title': 'MyWeb'})

# Create your views here.
