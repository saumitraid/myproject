from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    mobile=models.CharField(max_length=12)

class Contact(models.Model):
    fullname=models.CharField(max_length=255)
    email_id=models.CharField(max_length=255)
    message=models.TextField()
    def __str__(self):
            return self.fullname
