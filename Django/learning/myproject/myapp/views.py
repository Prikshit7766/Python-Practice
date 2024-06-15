from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature, DjangoCommand
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

# this is the index function

def index(request):
    commands = DjangoCommand.objects.all()
    context = {
        'page': 'Home Page',
        'topic': 'Learning Django',
        'commands': commands,
    }
    return render(request, 'index.html', context)

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

    features = Feature.objects.all()

    return render(request, "index_demo.html", {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')

    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = User.objects.filter(username=username, password=password)
        if user is not None:
            return redirect('index_demo')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, "login.html")
    
def logout(request):
    auth.logout(request)
    return redirect('index_demo')

def all_posts(request):
    post_list = [1,2,3,4,"prikshit", "hello"]
    return render(request, "all_posts.html", {'posts': post_list})

def post(request, slug):
    return render(request, "post.html", {'slug': slug})