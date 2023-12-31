from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserChangeForm
    model=CustomUser

# Register your models here.

admin.site.register(CustomUser,CustomUserAdmin)