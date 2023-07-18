from django.db import models


class Ingredient(models.Model):
    """
       Ingredient model

       Attributes:
            name (CharField): The name of the ingredient.
            quantity (CharField): The quantity or amount required.

    """
    name = models.CharField(max_length=100, db_comment="The name of the ingredient.")
    quantity = models.CharField(max_length=100, db_comment="The quantity or amount required.")


    def __str__(self):
        return f'{self.name} {self.quantity}'
