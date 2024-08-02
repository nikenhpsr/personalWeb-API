from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import BlogViewSet, BlogMediaViewSet
from projects.views import ProjectViewSet, ProjectMediaViewSet
from users.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Portfolio API",
      default_version='v1',
      description="API for personal portfolio with blog and projects",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'blog-media', BlogMediaViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'project-media', ProjectMediaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]