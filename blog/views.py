from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Handle traffic from homepage
# Return what the user should see
def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def myweb(request):
    return render(request, 'blog/myweb.html', {'title': 'MyWeb'})

# Create your views here.
