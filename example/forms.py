import datetime

from django import forms
from django.utils import timezone

from example import models


class CustomDateInput(forms.DateInput):
    input_type = "date"


class CustomTimeInput(forms.TimeInput):
    input_type = "time"


class ReminderForm(forms.ModelForm):
    class Meta:
        model = models.Reminder
        fields = ["name"]

    timestamp_date = forms.DateField(label="Date", widget=CustomDateInput)
    timestamp_time = forms.TimeField(label="Time", widget=CustomTimeInput)

    def save(self, commit=True):
        timestamp = timezone.make_aware(
            datetime.datetime.combine(
                self.cleaned_data["timestamp_date"],
                self.cleaned_data["timestamp_time"],
            )
        )
        self.instance.timestamp = timestamp
        return super().save(commit)
