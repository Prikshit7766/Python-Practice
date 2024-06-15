from django.contrib import admin
from .models import Feature, DjangoCommand, Book
# Register your models here.
admin.site.register(Feature)
admin.site.register(DjangoCommand)
admin.site.register(Book)