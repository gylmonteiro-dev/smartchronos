from .models import EntryTime
from django.contrib import admin

# Register your models here.

@admin.register(EntryTime)
class EntryTimeAdmin(admin.ModelAdmin):
    list_display = ('user__username',)