from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# this is the index function
def index(request):
    # name =  "Prikshit"
    context = {
        'name': "Prikshit",
        'age': 22,
        'city': "jammu"

    }
    return render(request, "index.html", context)