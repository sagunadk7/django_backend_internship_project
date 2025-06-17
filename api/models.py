# This is the models which store all the Telegram bot's username
from django.db import models
class User(models.Model):
        telegram_id = models.BigIntegerField(unique=True)
        username = models.CharField(max_length=150, null=True, blank=True)
        first_name = models.CharField(max_length=150, null=True, blank=True)
        last_name = models.CharField(max_length=150, null=True, blank=True)
        is_bot = models.BooleanField(default=False)
        language_code = models.CharField(max_length=10, null=True, blank=True)
        def __str__(self):
            return self.username or str(self.telegram_id)

# Create your models here.
