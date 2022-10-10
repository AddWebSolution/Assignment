from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserMasterManager


class UserMaster(AbstractBaseUser, PermissionsMixin):
    user = models.CharField(max_length=20)
    username = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserMasterManager()

    def __str__(self):
        return self.username


class ProgramMaster(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class UserProgram(models.Model):
    ACCESS_CHOICE = (
        (None, 'Select'),
        ('R', 'R'),
        ('W', 'W'),
        ('B', 'B'),
    )

    user = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    program = models.ManyToManyField(ProgramMaster, blank=True)
    access = models.CharField(max_length=2, choices=ACCESS_CHOICE, default=None)

    def __str__(self):
        return f"{self.user.user}'s (ACCESS: {self.access})"
