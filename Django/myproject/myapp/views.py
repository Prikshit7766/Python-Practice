from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# this is the index function
def index(request):
    return render(request, "index.html")