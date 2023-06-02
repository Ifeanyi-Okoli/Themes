from django.shortcuts import render
from django.views import generic, View

# Create your views here.

def home(request):
    return render(request, 'app/index.html', {})
        

def about(request):
    return render(request, 'app/blog-details.html', {})


def blog(request):
    return render(request, 'app/blog.html', {})
        

def services(request):
    return render(request, 'app/services-details.html', {})



def portfolio(request):
    return render(request, 'app/portfolio-details.html', {})

