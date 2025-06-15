# This is the models which store all the Telegram bot's username
from django.db import models
class User(models.Model):
    BotUser = models.CharField(max_length=100)


# Create your models here.
