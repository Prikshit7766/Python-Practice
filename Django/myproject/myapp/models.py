from django.db import models

# Create your models here.
# mostly used in configuring the database. we mostly don't need to write single line of sql code to get your database up and running, that what we have models vews templates

# from the mode we just pass all our data into templates file

class Feature:
    id: int
    name: str
    detail:str
    is_true: bool
    icon: str

    
    def __str__(self):
        return self.name