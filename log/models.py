from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Login(models.Model):
    login_title = models.CharField(max_length=200)