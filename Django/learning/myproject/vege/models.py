from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # This is a foreign key to the User model in Django which is used to store the user who created the recipe in the database.
    # The on_delete argument is used to specify what should happen if the user who created the recipe is deleted from the database. In this case, we are using SET_NULL which means that if the user is deleted, the user field in the Recipe model will be set to NULL.
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='images/')
    recipe_view_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.recipe_name
    

