# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Grading(models.Model):

    #__Grading_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Grading_FIELDS__END

    class Meta:
        verbose_name        = _("Grading")
        verbose_name_plural = _("Grading")


class Rank(models.Model):

    #__Rank_FIELDS__
    rank = models.CharField(max_length=255, null=True, blank=True)

    #__Rank_FIELDS__END

    class Meta:
        verbose_name        = _("Rank")
        verbose_name_plural = _("Rank")


class Trade(models.Model):

    #__Trade_FIELDS__
    trade = models.CharField(max_length=255, null=True, blank=True)

    #__Trade_FIELDS__END

    class Meta:
        verbose_name        = _("Trade")
        verbose_name_plural = _("Trade")


class Trainee(models.Model):

    #__Trainee_FIELDS__
    serviceno = models.CharField(max_length=255, null=True, blank=True)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Trainee_FIELDS__END

    class Meta:
        verbose_name        = _("Trainee")
        verbose_name_plural = _("Trainee")


class Cpt(models.Model):

    #__Cpt_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    run = models.IntegerField(null=True, blank=True)
    h-rope = models.IntegerField(null=True, blank=True)
    v-rope = models.IntegerField(null=True, blank=True)
    push-ups = models.IntegerField(null=True, blank=True)
    sit-ups = models.IntegerField(null=True, blank=True)
    totalpoints = models.IntegerField(null=True, blank=True)
    grading = models.ForeignKey(Grading, on_delete=models.CASCADE)
    result = models.CharField(max_length=255, null=True, blank=True)

    #__Cpt_FIELDS__END

    class Meta:
        verbose_name        = _("Cpt")
        verbose_name_plural = _("Cpt")



#__MODELS__END
