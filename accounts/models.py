from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER = (
        ("M", "male"),
        ("F", "female"),
    )
    address = models.TextField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

