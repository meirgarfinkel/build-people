from django.utils.translation import gettext_lazy as _
from django.db import models


class Roles(models.TextChoices):
    EMPLOYEE = ("EMPLOYEE", _("Employee"))
    EMPLOYER = ("EMPLOYER", _("Employer"))
    ADMIN = ("ADMIN", _("Admin"))
