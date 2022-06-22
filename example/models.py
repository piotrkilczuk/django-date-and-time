from django.db import models


class Reminder(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
