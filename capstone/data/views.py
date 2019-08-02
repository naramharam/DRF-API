from django.contrib.auth import get_user_model
from data.models import facilty, other, community, professional, jaega
from data.serializers import FaciltySerializer, OtherSerializer, CommunitySerializer,\
    ProfessionalSerializer, JaeGaSerializer
from django.contrib.auth.models import User
from data.serializers import UserSerializer
from rest_framework import permissions
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

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'users': reverse('user-list', request=request, format=format),
        'facilty': reverse('facilty-list', request=request, format=format),
        'jaega': reverse('jaega-list', request=request, format=format),
        'other': reverse('other-list', request=request, format=format),
        'community': reverse('community-list', request=request, format=format),
        'professional': reverse('professional-list', request=request, format=format)
     })


class FaciltyViewSet(viewsets.ModelViewSet):
    # 이 뷰셋은 'list'와 'create', 'retrieve', 'update', 'destory' 기능을 자동으로 지원한다.
    # 여기에 'highlight' 기능의 코드만 추가로 작성했다.
    queryset = facilty.objects.all()
    serializer_class = FaciltySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        facilty = self.get_object()
        return Response(facilty.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OtherViewSet(viewsets.ModelViewSet):
    # 이 뷰셋은 'list'와 'create', 'retrieve', 'update', 'destory' 기능을 자동으로 지원한다.
    # 여기에 'highlight' 기능의 코드만 추가로 작성했다.
    queryset = other.objects.all()
    serializer_class = OtherSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        other = self.get_object()
        return Response(other.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class JaeGaViewSet(viewsets.ModelViewSet):
    # 이 뷰셋은 'list'와 'create', 'retrieve', 'update', 'destory' 기능을 자동으로 지원한다.
    # 여기에 'highlight' 기능의 코드만 추가로 작성했다.
    queryset = jaega.objects.all()
    serializer_class = JaeGaSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        jaega = self.get_object()
        return Response(jaega.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommunityViewSet(viewsets.ModelViewSet):
    # 이 뷰셋은 'list'와 'create', 'retrieve', 'update', 'destory' 기능을 자동으로 지원한다.
    # 여기에 'highlight' 기능의 코드만 추가로 작성했다.
    queryset = community.objects.all()
    serializer_class = CommunitySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        community = self.get_object()
        return Response(community.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfessionalViewSet(viewsets.ModelViewSet):
    # 이 뷰셋은 'list'와 'create', 'retrieve', 'update', 'destory' 기능을 자동으로 지원한다.
    # 여기에 'highlight' 기능의 코드만 추가로 작성했다.
    queryset = professional.objects.all()
    serializer_class = ProfessionalSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        professional = self.get_object()
        return Response(professional.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

