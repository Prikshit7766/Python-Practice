from django.shortcuts import render
from django.http import HttpResponse

def student(request):
    return HttpResponse("Hello, world. You're at the college index.")
