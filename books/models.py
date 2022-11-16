from django.db import models
from .choices import StatusChoice


# Create your models here.

class Books(models.Model):
    bookName = models.CharField(max_length=200, null=False, help_text='This field is required')
    status = models.CharField(max_length=100, choices=StatusChoice.choices, default=StatusChoice.TO_READ)

    def __str__(self):
        return self.bookName
