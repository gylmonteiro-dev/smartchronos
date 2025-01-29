from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    registration = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    
    
    
    # problema com a criação do usuário e a senha
    def __str__(self):
        return self.username