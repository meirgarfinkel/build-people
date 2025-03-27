from django.db import models
import uuid
from shared.model_mixins import TimestampedModelMixin


class Company(TimestampedModelMixin):
    """
    Company model that represents the organization.
    """
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        "users.USER",
        on_delete=models.CASCADE,
        related_name="companies"
    )

    def __str__(self):
        return self.name


class EmployeeInvite(TimestampedModelMixin):
    company = models.ForeignKey("gratify.Company", on_delete=models.CASCADE, related_name="invites")
    email = models.EmailField()
    token = models.UUIDField(default=uuid.uuid4, unique=True)  # Unique invite token
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.email
