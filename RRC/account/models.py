from django.db import models

# Create your models here.


class User(models.Model):
    created = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=100, blank=False, default='')
    password = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['created']