from django.db import models


class Humidity(models.Model):
    rangomed = models.IntegerField(max_length=950, blank=True, null=True)


class Gas(models.Model):
    ppm = models.IntegerField(max_length=None, blank=True, null=True)


class Temperature(models.Model):
    celcuis = models.IntegerField(max_length=30, blank=True, null=True)
