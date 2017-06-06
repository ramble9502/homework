from django.db import models


from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    Gender_CHOICES = (
        (1, "FEMALE"),
        (2, "MALE"),
    )
    user = models.OneToOneField(User, related_name="userprofile")
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=20)
    sex = models.PositiveSmallIntegerField(choices=Gender_CHOICES, default=1)

    def __unicode__(self):
        return self.user.username


class Lmessage(models.Model):
    user = models.ForeignKey(User, related_name="lmessage")
    comment = models.CharField(max_length=500)
    datetime = models.DateTimeField()

    def __unicode__(self):
        return self.user


class Divescore(models.Model):
    user = models.ForeignKey(User, related_name="divescore")
    score = models.CharField(max_length=10)
    datetime = models.DateTimeField()

    def __unicode__(self):
        return self.user


class Testscore(models.Model):
    user = models.ForeignKey(User, related_name="testscore")
    score = models.CharField(max_length=10)
    datetime = models.DateTimeField()

    def __unicode__(self):
        return self.user


class StoryOfBartender(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=500)
    picture = models.URLField()

    def __unicode__(self):
        return self.title


class BrewWine(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=2000)
    picture = models.URLField()

    def __unicode__(self):
        return self.title


class Test(models.Model):
    head = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    answer = models.CharField(max_length=5)

    def __unicode__(self):
        return self.title


class Testoption(models.Model):
    contact = models.ForeignKey(Test, related_name="testoption")
    optiontitle = models.CharField(max_length=10)
    optioncontent = models.CharField(max_length=50)
    optionvalue = models.CharField(max_length=5)
