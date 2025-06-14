from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from api.mypagination import MyLimitoffsetPagination
from api.models import User
from api.serializers import UserSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication

# This is public view for public api , public can only read it
class PublicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]
    pagination_class = MyLimitoffsetPagination


# This is the protected view for authenticated users only and give full CRUD access to all items
class ProtectedViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = MyLimitoffsetPagination
    authentication_classes = [JWTAuthentication]


# Create your views here.
