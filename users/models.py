from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.constants import Levels


class User(AbstractUser):
    employee_id = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to="images/profile_photo/%Y/%m/%d/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20, null=True, blank=True)
    level = models.IntegerField(choices=Levels.choices, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username