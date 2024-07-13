from django.urls import path
from . import views  # Ensure that views is imported

urlpatterns = [
    path('', views.student, name='student'),  
]
