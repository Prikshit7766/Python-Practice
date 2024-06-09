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

def counter_page(request):
    return render(request, "counter_page.html") 

def count(request):
    text = request.GET['text']
    words = text.split()
    word_count = len(words)
    return render(request, "count.html", {'text': text, 'word_count': word_count})


def count(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        words = text.split()
        word_count = len(words)
        return render(request, "count.html", {'text': text, 'word_count': word_count})
    else:
        return HttpResponse("Method not allowed")
    
def index_demo(request):
    return render(request, "index_demo.html")