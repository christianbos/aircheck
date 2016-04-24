from django.db import models


class Humidity(models.Model):
    rangomed = models.FloatField(max_length=950, blank=True, null=True)


class Gas(models.Model):
    ppm = models.FloatField(max_length=None, blank=True, null=True)


class Temperature(models.Model):
    celsius = models.FloatField(max_length=30, blank=True, null=True)
