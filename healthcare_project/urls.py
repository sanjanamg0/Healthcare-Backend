from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clinic.views import RegisterView, DoctorViewSet, PatientViewSet, MappingViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# The router automatically creates all the GET/POST/PUT/DELETE paths for us!
router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'mappings', MappingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', RegisterView.as_view(), name='auth_register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # This includes all our doctor, patient, and mapping routes 
    path('api/', include(router.urls)), 
]