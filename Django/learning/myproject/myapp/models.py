from django.db import models

# Create your models here.
# mostly used in configuring the database. we mostly don't need to write single line of sql code to get your database up and running, that what we have models vews templates

# from the mode we just pass all our data into templates file

class Feature(models.Model): 

    name: str = models.CharField(max_length=150)
    detail:str = models.TextField()
    is_true: bool = models.BooleanField()
    icon: str = models.CharField(max_length=100)

    def __str__(self):
        return self.name # this is what will be displayed in the admin panel


class DjangoCommand(models.Model):
    command = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.command  # this is what will be displayed in the admin panel


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title
