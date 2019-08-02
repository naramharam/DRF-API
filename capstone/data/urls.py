from django.urls import path, include
from rest_framework.routers import DefaultRouter
from data import views

# 라우터를 생성하고 뷰셋을 등록한다.
router = DefaultRouter()
router.register(r'other', views.OtherViewSet)
router.register(r'facilty', views.FaciltyViewSet)
router.register(r'community', views.CommunityViewSet)
router.register(r'professional', views.ProfessionalViewSet)
router.register(r'jaega', views.JaeGaViewSet)
router.register(r'users', views.UserViewSet)

# API URL을 라우터가 자동으로 인식한다.
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
]