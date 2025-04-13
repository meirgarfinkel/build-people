from django.db import models
import uuid
from shared.model_mixins import TimestampedModelMixin
from django.conf import settings


class Company(TimestampedModelMixin):
    """
    Company model that represents the organization.
    """
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, related_name="owned_companies")

    def __str__(self):
        return self.name


class EmployeeInvite(TimestampedModelMixin):
    company = models.ForeignKey("build_people.Company", on_delete=models.CASCADE, related_name="invites")
    email = models.EmailField()
    token = models.UUIDField(default=uuid.uuid4, unique=True)  # Unique invite token
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Recognition(TimestampedModelMixin):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recognitions")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_recognitions")
    message = models.TextField()
    points = models.PositiveIntegerField()
    hearts = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="hearted_recognitions",
        blank=True,
        help_text="Users who liked this recognition"
    )

    def __str__(self):
        return f"{self.created_by} -> {self.receiver}"


class RecognitionComment(TimestampedModelMixin):
    recognition = models.ForeignKey(
        Recognition,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content = models.TextField(help_text="Comment content")

    def __str__(self):
        return f"Comment by {self.user} on {self.recognition}"
    
    class Meta:
        ordering = ["-created_at"]
