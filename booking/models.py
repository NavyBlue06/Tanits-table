from django.db import models
from datetime import date
from django.core.exceptions import ValidationError


def validate_future_date(value):
    """Prevents booking dates in the past."""
    if value < date.today():
        raise ValidationError("Booking date cannot be in the past.")


class Booking(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(validators=[validate_future_date])
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
