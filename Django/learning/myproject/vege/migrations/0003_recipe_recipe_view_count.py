# Generated by Django 4.2.13 on 2024-07-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vege", "0002_recipe_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="recipe_view_count",
            field=models.IntegerField(default=0),
        ),
    ]
