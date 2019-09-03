from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from data import views

# 라우터를 생성하고 뷰셋을 등록한다.
from data.views import UserViewSet

router = DefaultRouter(trailing_slash=True)
router.register(r'all', views.AllViewSet)
router.register(r'other', views.OtherViewSet)
router.register(r'facility', views.FacilityViewSet)
router.register(r'community', views.CommunityViewSet)
router.register(r'professional', views.ProfessionalViewSet)
router.register(r'jaega', views.JaeGaViewSet)
router.register(r'account', views.UserViewSet)
# router.register(r'login', views.LoginViewSet)


# API URL을 라우터가 자동으로 인식한다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
