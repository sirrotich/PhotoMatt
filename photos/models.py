from django.db import models

# Create your models here.
class Location(models.Model):
    first_name = models.CharField(max_length =25)

    def __str__(self):
        return self.first_name

    def save_location(self):
        self.save()

    class Meta:
        ordering = ['first_name']