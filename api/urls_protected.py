# This is the urls for protected api endpoints
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ProtectedViewSet


router = DefaultRouter()
router.register('items',ProtectedViewSet, basename='public-items')
urlpatterns = [
    path('protected/api/',include(router.urls))
]