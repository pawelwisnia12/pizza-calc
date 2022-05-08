from django.db import models


class Pizza(models.Model):
    type = models.CharField(max_length=100)
    published_date = models.DateField("Date published")
