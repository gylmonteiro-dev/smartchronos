from django.db import models
from accounts.models import CustomUser
# Create your models here.
class EntryTime(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} : {self.created_at.date()} | {self.created_at.hour}:{self.created_at.minute}"