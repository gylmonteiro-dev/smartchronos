from .models import CustomUser
from django.contrib import admin

# Register your models here.

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'first_name', 'registration')
#     list_filter = ('username', 'registration', 'first_name')


admin.site.register(CustomUser)