from email.policy import default
from django.db import models


class House(models.Model):

    """House Definition for Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price", help_text="Positive numbers only...")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True, help_text="Does this house allow pets?")

    def __str__(self):
        return self.name
