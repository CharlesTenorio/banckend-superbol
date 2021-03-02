from django.contrib import admin
from django.urls import path
from times.views import get_times
from ligas.views import get_ligas
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
      openapi.Info(
         title="SuperBol API",
         default_version='v1',
         description="Documentacao",
         terms_of_service="https://www.google.com/policies/terms/",
         contact=openapi.Contact(email="contact@snippets.local"),
         license=openapi.License(name="BSD License"),
      ),
      public=True,
      permission_classes=(permissions.AllowAny,),
   )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_times/', get_times, name='get_times'),
    path('get_ligas/', get_ligas, name='get_ligas'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]



admin.site.site_header = "Super Boll"

admin.site.index_title = "Super Boll"

admin.site.site_title = "Super Boll"
