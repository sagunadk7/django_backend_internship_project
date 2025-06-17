from django.contrib import admin
from api.models import User
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['id','telegram_id','username','first_name','last_name','is_bot','language_code']

