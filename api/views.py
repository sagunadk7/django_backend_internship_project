from django.shortcuts import render
from rest_framework.generics import ModelViewSet

class UserModelViewSets(viewset.ModelViewSet):
    qureyset = User.objects.all()
    serializers = UserSerializer

# Create your views here.
