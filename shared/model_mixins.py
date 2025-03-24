from django.db import models


class TimestampedModelMixin(models.Model):
    """
    Mixin to add `created_at` and `updated_at` fields to a model
    """

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
