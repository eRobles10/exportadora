from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)
    rfc = models.TextField(max_length=50, null=True, blank=True)
    phone = models.TextField(max_length=20, null=True, blank=True)
