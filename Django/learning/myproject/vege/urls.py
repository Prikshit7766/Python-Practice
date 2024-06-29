from django.urls import path
from . import views


urlpatterns = [
    path('', views.recipe, name="recipe"),
    path('perform_action/', views.perform_action, name='perform_action'),
    path('update/<int:id>/', views.update_recipe, name='update_recipe'),
]
