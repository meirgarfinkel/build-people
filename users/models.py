from django.db import models
from django.contrib.auth.models import AbstractUser

from shared.model_mixins import TimestampedModelMixin


class User(AbstractUser, TimestampedModelMixin):
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
