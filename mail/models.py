from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
import uuid


class Marketing(models.Model):
    name = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.ForeignKey(User, related_name='customers', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.email)


class Promotion(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    marketing = models.ForeignKey(Marketing, related_name='promotions', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='promotions', on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} {1}'.format(self.marketing, self.customer)


class Settings(models.Model):
    user = models.ForeignKey(User, related_name='settings', on_delete=models.CASCADE)
    email = models.EmailField(blank=False)
    smtp_key = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.email
