from django.db import models
import uuid


class Marketing(models.Model):
    name = models.CharField(max_length=100, unique=True)
    message = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    marketing = models.ForeignKey(Marketing, related_name='promotions', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='promotions', on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(blank=False)
