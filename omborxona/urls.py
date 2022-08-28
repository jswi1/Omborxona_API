from django.contrib import admin
from django.urls import path
from rest_framework.schemas import openapi, get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Omborxona API",
      default_version='v1',
      description="Omborxona DRF",
      contact=openapi.Contact("Muhammadqodir. Email: <muhammadqodir228@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name="swagger"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
