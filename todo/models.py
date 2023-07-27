"Libraries"
from django.db import models

# pylint:disable = E0307

# Create your models here.


class Item(models.Model):
    "Set up db model for Item"
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
