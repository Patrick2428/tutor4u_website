from typing import Text
from django.db import models
from django.db.models.fields import NullBooleanField
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User


class UserPersona(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
class UserProfile(models.Model):
    # owner
    user = OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    is_full_name_displayed = models.BooleanField(default=True)

    # details
    # next_lesson = models.CharField(max_length=500, blank=True, null=True)
    next_lesson = models.DateTimeField(null=True)
    school = models.CharField(max_length=64, blank=True, null=True)
    grade = models.IntegerField(null=True)
    persona = models.ForeignKey(
        UserPersona, on_delete=models.SET_NULL, blank=True, null=True
    )
