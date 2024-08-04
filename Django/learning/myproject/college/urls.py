from django.urls import path
from . import views

urlpatterns = [
    path('', views.college, name='college'),
    path('student/', views.student, name='student_list'),
]
