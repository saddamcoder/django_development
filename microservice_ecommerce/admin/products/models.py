from django.db import models
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'products'


class User(models.Model):
    pass