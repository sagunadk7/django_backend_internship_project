from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import(
TokenObtainPairView,
TokenRefreshView,
TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenObtainPairView.as_view(),name='token_refresh'),
    path('api/token/verify/',TokenVerifyView.as_view(),name='token-verify'),
    path('',include('api.urls_protected')),
    path('',include('api.urls_public')),
    path('',include('users.user_urls'))
]
