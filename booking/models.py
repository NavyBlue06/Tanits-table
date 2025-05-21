from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
