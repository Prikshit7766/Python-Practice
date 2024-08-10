from django.urls import path
from . import views

urlpatterns = [
    path('', views.college, name='college'),
    path('student/', views.student, name='student_list'),
    path('student/<int:student_id>/', views.see_marks, name='see_marks'), 
]
