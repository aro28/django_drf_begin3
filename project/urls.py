
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Backend for my online shop API",
      default_version='alpha-0.0.1',
      description="This is API for online shop",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="prostotak1981@gmail.com"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
swagger_urlpatterns =[
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('doctor.urls')),
] + swagger_urlpatterns
