from datetime import date, datetime
from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(default=datetime.today)
    estimated_end = models.DateField(blank=True, null=True)
    priority = models.IntegerField(default=3)

    def __str__(self):
        return self.title
    