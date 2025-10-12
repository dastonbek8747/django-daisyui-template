from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Fanlar(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Test(models.Model):
    fanlar = ForeignKey(Fanlar, on_delete=models.CASCADE, related_name='tests')
    request = models.CharField(max_length=500, null=True, blank=True)
    response_a = models.CharField(max_length=500, null=True, blank=True)
    response_b = models.CharField(max_length=500, null=True, blank=True)
    response_c = models.CharField(max_length=500, null=True, blank=True)
    response_d = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.request


class Users(models.Model):
    name = models.TextField(max_length=500, null=True, blank=True)
    email = models.TextField(max_length=500, null=True, blank=True)
    password = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


