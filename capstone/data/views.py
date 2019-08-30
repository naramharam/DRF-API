from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from data.models import Facility, Other, community, professional, Jaega, all, UserModel
from data.serializers import FaciltySerializer, OtherSerializer, CommunitySerializer,\
    ProfessionalSerializer, JaeGaSerializer, AllSerializer, UserSerializer
from django.contrib.auth.models import User
# from data.serializers import UserSerializer
from rest_framework import permissions, status
from data.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     # 이 뷰셋은 'list'와 'detail' 기능을 자동으로 지원한다.
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

    # def perform_create(self, serializer):
    #     password = make_password(self.request.data['password'])
    #     serializer.save(password=password)
#


@api_view(['GET', 'POST'])
def api_root(request, format=None):
    print(request)
    if request.method == 'GET':
        return Response({
            'accounts': reverse('accounts-list', request=request, format=format),
            'facility': reverse('facility-list', request=request, format=format),
            'jaega': reverse('jaega-list', request=request, format=format),
            'other': reverse('other-list', request=request, format=format),
            'community': reverse('community-list', request=request, format=format),
            'professional': reverse('professional-list', request=request, format=format),
            # 'accounts': reverse('accounts-list', request=request, format=format)
         })
    elif request.method == 'POST':
        pass


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = UserModel.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, args, kwargs)


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FaciltySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class OtherViewSet(viewsets.ModelViewSet):
    queryset = Other.objects.all()
    serializer_class = OtherSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class JaeGaViewSet(viewsets.ModelViewSet):
    queryset = Jaega.objects.all()
    serializer_class = JaeGaSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = community.objects.all()
    serializer_class = CommunitySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = professional.objects.all()
    serializer_class = ProfessionalSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class AllViewSet(viewsets.ModelViewSet):
    queryset = all.objects.all()
    serializer_class = AllSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

