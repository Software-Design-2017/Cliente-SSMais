from django.contrib import admin

from .models import (
    ServiceHair, ServiceBeard
)

admin.site.register(ServiceHair)
admin.site.register(ServiceBeard)
