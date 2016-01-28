#coding: utf-8

from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Audio(models.Model):
    name = models.CharField(max_length=50)
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    url = models.CharField(max_length=200)
