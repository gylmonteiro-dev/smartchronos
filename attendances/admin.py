from .models import WorkPointRecord
from django.contrib import admin

# Register your models here.

@admin.register(WorkPointRecord)
class EntryTimeAdmin(admin.ModelAdmin):
    list_display = ('user__username',)