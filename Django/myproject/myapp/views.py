from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

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
    # create 4 features 
    feature1 = Feature()
    feature1.id = 1
    feature1.name = "Fast"
    feature1.detail = "This is a fast feature"
    feature1.is_true = True
    feature1.icon = "bi bi-gem"

    feature2 = Feature()
    feature2.id = 2
    feature2.name = "Secure"
    feature2.detail = "This is a secure feature"
    feature2.is_true = True
    feature2.icon = "bi bi-lock"

    feature3 = Feature()
    feature3.id = 3
    feature3.name = "Reliable"
    feature3.detail = "This is a reliable feature"
    feature3.is_true = False
    feature3.icon = "bi bi-book"

    feature4 = Feature()
    feature4.id = 4
    feature4.name = "Scalable"
    feature4.detail = "This is a scalable feature"
    feature4.is_true = True
    feature4.icon = "bi bi-arrows-expand"

    features = [feature1, feature2, feature3, feature4]

    return render(request, "index_demo.html", {'features': features})