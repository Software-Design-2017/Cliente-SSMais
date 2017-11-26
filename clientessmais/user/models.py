import datetime

# Django.
from django.db import models
from ssmais.search_scheduling.models import User
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, name, **kwargs):
        if not email:
            raise ValueError('The given email must be set')

        user = self.model(email=self.normalize_email(email),
                          name=name,
                          is_active=False,
                          **kwargs)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, name, **kwargs):
        user = self.model(email=self.normalize_email(email),
                          name=name,
                          is_staff=True,
                          is_active=True,
                          is_superuser=True,
                          **kwargs)

        user.set_password(password)
        user.save(using=self.db)

        return user


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = u'Perfil de Usuario'


class Client(User):
    phone_number = models.CharField(max_length=100)

    objects = UserManager()

    def __str__(self):
        return self.phone_number
