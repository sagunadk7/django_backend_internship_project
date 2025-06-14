# This the urls for public api endpoints
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PublicViewSet
router = DefaultRouter()
router.register('items',PublicViewSet, basename='public-items')
urlpatterns = [
    path('public/api/',include(router.urls))
]