# django
from django.db import models

# third party
from ssmais.search_scheduling.models import Service

# Local Django
from . import (
    constants, validators
)


class ServiceHair(Service):
    specific_hair = models.PositiveIntegerField(validators=[validators.validate_specific_hair],
                                                choices=constants.SPECIFIC_HAIR_CHOICES)
    style = models.CharField(validators=[validators.validate_style], max_length=120)


class ServiceBeard(Service):
    style = models.CharField(validators=[validators.validate_style], max_length=120)
