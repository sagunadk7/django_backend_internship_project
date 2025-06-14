from django.contrib import admin
from api.models import User
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['id','BotUser']

