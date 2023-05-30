from django.shortcuts import render
from django.views import generic, View
# Create your views here.

def home(request):
    return render(request, 'app/index.html', {})