from functools import cached_property
from django.db import models
from django.contrib.auth.models import AbstractUser
from users.enums import Roles
from django.utils.translation import gettext_lazy as _
from shared.model_mixins import TimestampedModelMixin


class User(AbstractUser, TimestampedModelMixin):
    """
    Custom user model that can be either an Owner or an Employee.
    """
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(_("company position"),max_length=10, choices=Roles.choices, default=Roles.EMPLOYEE)
    company = models.ForeignKey("build_people.Company", on_delete=models.PROTECT, related_name="members")
    points_available = models.PositiveIntegerField(default=100)
    points_received = models.PositiveIntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def is_admin(self):
        return self.role == Roles.EMPLOYER
