from django.shortcuts import render
from .models import Recipe
from django.shortcuts import redirect

# Create your views here.

def recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES['recipe_image']

        Recipe.objects.create(recipe_name=recipe_name, recipe_description=recipe_description, recipe_image=recipe_image)

        return redirect('recipe')

    # display the recipe
    recipes = Recipe.objects.all()
    return render(request, 'vege/recipe.html', {'recipes': recipes})

def perform_action(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        selected_recipes = request.POST.getlist('selected_recipes')
        
        if action == 'delete':
            Recipe.objects.filter(id__in=selected_recipes).delete()
        
        
    return redirect('recipe')