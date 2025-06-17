from api.models import User
from rest_framework import serializers
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class DetailedUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','telegram_id','username','first_name','last_name','is_bot','language_code']

