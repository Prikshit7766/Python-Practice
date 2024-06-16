from django.shortcuts import render
from .models import Recipe

# Create your views here.

def recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES['recipe_image']

        Recipe.objects.create(recipe_name=recipe_name, recipe_description=recipe_description, recipe_image=recipe_image)

    return render(request, 'vege/recipe.html')
