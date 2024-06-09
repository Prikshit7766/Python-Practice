from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), # this is root URL, this will call the index function from views.py 

]


# suppose if the user comenst to any particular URL then what will happen ?
# we render a html file, can can send an http or  a json response (anything) that is going to happen in the views.py file
