from django.db import models

class House(models.Model):
    """
    Represents a Hogwarts house with its unique attributes.
    """
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="The name of the house (e.g., Gryffindor, Slytherin)."
    )
    colors = models.CharField(
        max_length=100,
        default="Unknown",
        help_text="The house colors (e.g., Scarlet and Gold)."
    )
    animal = models.CharField(
        max_length=50,
        default="Unknown",
        help_text="The animal symbol of the house (e.g., Lion)."
    )
    founder = models.CharField(
        max_length=50,
        default="Unknown",
        help_text="The founder of the house (e.g., Godric Gryffindor)."
    )
    traits = models.TextField(
        default="Unknown",
        help_text="Key traits associated with this house (e.g., Bravery, Loyalty)."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "House"
        verbose_name_plural = "Houses"
