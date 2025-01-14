from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class WorkPointRecord(models.Model):

    TYPE_REGISTER = (
        ('I', 'Entrada'),
        ('O', 'Saída')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="point_records")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    type_point = models.CharField(max_length=1, choices=TYPE_REGISTER, default='I')
    valid = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user.username} : {self.created_at.date()} | {self.created_at.hour}:{self.created_at.minute}"
