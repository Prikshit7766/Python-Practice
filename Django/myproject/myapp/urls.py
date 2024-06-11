from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), # this is root URL, this will call the index function from views.py 
    path('counter_page', views.counter_page, name="counter_page"),
    path('count', views.count, name="count"), 
    path('index_demo', views.index_demo, name="index_demo"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('all_posts', views.all_posts, name="all_posts"),
    path('post/<str:slug>', views.post, name="post"),
]

# suppose if the user comenst to any particular URL then what will happen ?
# we render a html file, can can send an http or  a json response (anything) that is going to happen in the views.py file
