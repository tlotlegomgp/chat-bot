from django.contrib import admin
from .models import UserQuery

# Register your models here.

class UserQueryAdmin(admin.ModelAdmin):
    list_display = ('body', 'date')


admin.site.register(UserQuery, UserQueryAdmin)