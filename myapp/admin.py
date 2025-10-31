# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser

# Register your models here
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'google', 'facebook','location','profile_pic_url')
