from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.CharField(max_length=30, blank=True, null=True)
    twitter = models.CharField(max_length=256, blank=True, null=True)
