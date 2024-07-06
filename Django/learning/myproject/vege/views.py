from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES['recipe_image']

        Recipe.objects.create(recipe_name=recipe_name, recipe_description=recipe_description, recipe_image=recipe_image)
        return redirect('recipe')

    recipes = Recipe.objects.all()
    return render(request, 'vege/recipe.html', {'recipes': recipes})

def perform_action(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        selected_recipes = request.POST.getlist('selected_recipes')
        
        if action == 'delete':
            Recipe.objects.filter(id__in=selected_recipes).delete()
    return redirect('recipe')

def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    
    if request.method == 'POST':
        recipe.recipe_name = request.POST.get('recipe_name')
        recipe.recipe_description = request.POST.get('recipe_description')
        if 'recipe_image' in request.FILES:
            recipe.recipe_image = request.FILES['recipe_image']
        recipe.save()
        return redirect('recipe')
    
    return render(request, 'vege/update_recipe.html', {'recipe': recipe})

def search_recipes(request):
    query = request.GET.get('search')
    if query:
        recipes = Recipe.objects.filter(
            Q(recipe_name__icontains=query) |
            Q(recipe_description__icontains=query)
        )
    else:
        recipes = Recipe.objects.all()
    
    return render(request, 'vege/search_results.html', {'recipes': recipes})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Registered")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username, email=email,
                )
                user.set_password(password)
                user.save()
                return redirect("login")
        else:
            messages.info(request, "Password Not Matching")
            return redirect("register")

    return render(request, "vege/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("recipe")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")
    else:
        return render(request, "vege/login.html")