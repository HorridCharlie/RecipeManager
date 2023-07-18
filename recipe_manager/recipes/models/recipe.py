from django.db import models
from . import Chef
from . import Ingredient
from . import Category



class Recipe(models.Model):
    """
       Recipe model

       Attributes:
            title (CharField): The title of the recipe.
            description (TextField): A description or instructions for the recipe.
            chef (ForeignKey to Chef): The chef who created the recipe.
            ingredients (ManyToManyField to Ingredient): The ingredients required for the recipe.
            categories (ManyToManyField to Category): The categories to which the recipe belongs.
            created_at (DateTimeField): The timestamp when the recipe was created.

    """
    title = models.CharField(max_length=100, db_comment="The title of the recipe.")
    description = models.TextField(db_comment="A description or instructions for the recipe.")
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, db_comment="The chef who created the recipe.")
    ingredients = models.ManyToManyField(Ingredient, db_comment="The ingredients required for the recipe.")
    categories = models.ManyToManyField(Category, db_comment="The categories to which the recipe belongs.")
    created_at = models.DateTimeField(auto_now_add=True, db_comment="The timestamp when the recipe was created.")

    def __str__(self):
        return f'{self.title} {self.description} {self.chef} {self.ingredients} {self.categories} {self.created_at}'
