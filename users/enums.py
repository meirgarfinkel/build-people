from django.utils.translation import gettext_lazy as _
from django.db import models


class Roles(models.TextChoices):
    EMPLOYEE = ("EMPLOYEE", _("Employee"))
    EMPLOYER = ("EMPLOYER", _("Employer"))
    ADMIN = ("ADMIN", _("Admin"))


class RecognitionPoints(models.TextChoices):
    TEN = ("10", _("10"))
    TWENTY = ("20", _("20"))
    THIRTY = ("30", _("30"))
    FORTY = ("40", _("40"))
    FIFTY = ("50", _("50")
)
