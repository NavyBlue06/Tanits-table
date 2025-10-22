from datetime import date
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "email", "date", "time", "guests"]
        widgets = {
            "date": DateInput(),
            "time": TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        # Accept current user so we can check duplicates nicely
        self.request_user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        # UX: stop the browser from picking past dates
        self.fields["date"].widget.attrs["min"] = date.today().isoformat()

    def clean_date(self):
        d = self.cleaned_data["date"]
        if d < date.today():
            raise forms.ValidationError("You cannot book a date in the past.")
        return d

    def clean(self):
        cleaned = super().clean()
        d = cleaned.get("date")
        t = cleaned.get("time")

        # Friendly duplicate check before the DB constraint fires
        if self.request_user and d and t:
            qs = Booking.objects.filter(user=self.request_user, date=d, time=t)
            if self.instance and self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError(
                    "There is already a booking for this date and time."
                )
        return cleaned
