from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import *


# Create your models here.


class DegreeCourse(models.Model):
    name = models.CharField(max_length=32)


class Course(models.Model):
    name = models.CharField(max_length=32)
    policy_list = GenericRelation(to="PricePolicy")


class PricePolicy(models.Model):
    period = models.IntegerField(choices=((1, "10天"), (2, "20天"),
                                          (3, "30天")))
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    course_obj = GenericForeignKey('content_type', 'object_id')
    price = models.DecimalField(max_digits=5, decimal_places=2)
