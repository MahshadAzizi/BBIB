from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    branches = (
        ('100', '100'),
        ('101', '101'),
        ('102', '102')
    )
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    national_code = models.CharField(max_length=20, null=True)
    branch_code = models.CharField(max_length=3, choices=branches)

    def save(self, *args, **kwargs):
        self.crew_password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
