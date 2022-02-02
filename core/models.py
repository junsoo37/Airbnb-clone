from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)   # object가 first create될 때마다 set함. auto_now_add가 True인 경우 해당 field를 변경할 수 없음.
    updated = models.DateTimeField(auto_now=True)   # object가 save 될 때마다 field를 update함

    class Meta:
        abstract = True