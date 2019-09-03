from django.db import models
from django.contrib.auth.models import AbstractUser


class Other(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    contents = models.TextField()
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Jaega(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    contents = models.TextField()
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Professional(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    contents = models.TextField()
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Community(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    contents = models.TextField()
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Facility(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    contents = models.TextField()
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class All(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    contents = models.TextField()
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class UserModel(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    user_id = models.EmailField()
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    sub_location = models.CharField(max_length=10)
    priority_volunteer = models.CharField(max_length=10)

#
# class LoginUserModel(models.Model):
#     user_id = models.EmailField()
#     password = models.CharField(max_length=100)
#

