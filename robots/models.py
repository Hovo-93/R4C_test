from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)
    in_stock = models.BooleanField(default=False)  # в наличии

    def __str__(self):
        return f'{self.model} - {self.version}'
