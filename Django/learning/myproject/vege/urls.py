from django.urls import path
from . import views


urlpatterns = [
    path('', views.recipe, name="recipe"),
    path('perform_action/', views.perform_action, name='perform_action'),
    path('update/<int:id>/', views.update_recipe, name='update_recipe'),
    path('search/', views.search_recipes, name='search_recipes'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
