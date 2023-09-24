import django
from django.db import models
from rest_framework import serializers


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(100)
    description = models.CharField(250)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
