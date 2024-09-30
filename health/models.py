from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.

class RegistrationForm(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(RegistrationForm, self).save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
