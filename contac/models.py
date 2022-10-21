from datetime import date, datetime
from email.policy import default
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=80, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    mobile = models.CharField(max_length=12, null=False, blank=True)
    email = models.EmailField(max_length=30, null=False, blank=True)
    date = models.DateField(default=datetime.today)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
