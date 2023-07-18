from django.db import models


class Category(models.Model):
    """
       Category model

       Attributes:
            name (CharField): The name of the category.

    """
    name = models.CharField(max_length=100, db_comment="The name of the category.")

    def __str__(self):
        return f'{self.name}'
