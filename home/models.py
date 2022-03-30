from django.db import models


# Create your models here.
class Member(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Ph = models.IntegerField(null=True, blank=True)
    Height = models.IntegerField(null=True, blank=True)
    Weight = models.IntegerField(null=True, blank=True)


class Feedback(models.Model):
    NAMAM = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=100)
