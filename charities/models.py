from django.db import models
from accounts.models import User

class Benefactor(models.Model):
    LOW = 0
    NORMAL = 1
    HIGH = 2
    EXPERIENCE = (
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
    )
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    experience = models.SmallIntegerField(choices=EXPERIENCE, default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name =  models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class Task(models.Model):
    STATE = (
        ("P", "Pending"),
        ("W", "Waiting"),
        ("A", "Assigned"),
        ("D", "Done"),
    )
    GENDER = (
        ("M", "male"),
        ("F", "female"),
    )
    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.SET_NULL, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.DO_NOTHING)
    age_limit_from = models.IntegerField(blank=True, null=True)
    age_limit_to = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender_limit = models.CharField(max_length=1, choices=GENDER, blank=True, null=True)
    state = models.CharField(max_length=1, choices=STATE)
    title = models.CharField(max_length=100)
