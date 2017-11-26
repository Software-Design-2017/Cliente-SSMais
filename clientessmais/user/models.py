from django.db import models

# Create your models here.
from ssmais.user.models import User as UserBase

class User(UserBase): pass
