from django.db import models
from account.models import User


class Item(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    img = models.URLField()
    author = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE)
    mcversion = models.CharField(max_length=10, blank=True, default='all')
    download_link = models.URLField()
    clock_time = models.CharField(max_length=100)


class ExtraItem(models.Model):
    pass