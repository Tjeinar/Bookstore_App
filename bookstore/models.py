from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50, default = "")
    image = models.ImageField(null=True, blank=True)
    price = models.CharField(max_length = 50, default = "")
    description = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(default=timezone.now)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
