from django.contrib import admin
from .models import Marketing, Customer, Promotion, Settings

# Register your models here.
admin.site.register((Marketing, Customer, Promotion, Settings))
