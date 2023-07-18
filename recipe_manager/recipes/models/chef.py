from django.db import models


class Chef(models.Model):
    """
       Chef model

       Attributes:
            name (CharField): The name of the chef.
            bio (TextField): A brief biography or description of the chef.

    """
    name = models.CharField(max_length=100, db_comment="The name of the chef.")
    bio = models.TextField(db_comment="A brief biography or description of the chef.")

    def __str__(self):
        return f'{self.name} {self.bio}'
