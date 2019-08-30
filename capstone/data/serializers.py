from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from data.models import Facility, Other, community, Jaega, professional, all, UserModel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = '__all__'


class FaciltySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='facilty-highlight', format='html')

    class Meta:
        model = Facility
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'location', 'sub_location', 'gender', 'contents']


class OtherSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='other-highlight', format='html')

    class Meta:
        model = Other
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'location', 'sub_location', 'gender', 'contents']


class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='community-highlight', format='html')

    class Meta:
        model = community
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'location', 'sub_location', 'gender', 'contents']


class JaeGaSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='jaega-highlight', format='html')

    class Meta:
        model = Jaega
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'location', 'sub_location', 'gender', 'contents']


class ProfessionalSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='professional-highlight', format='html')

    class Meta:
        model = professional
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'location', 'sub_location', 'gender', 'contents']


class AllSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='all-highlight', format='html')

    class Meta:
        model = all
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'location', 'sub_location', 'gender', 'contents']

#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     facilty = serializers.HyperlinkedRelatedField(many=True, view_name='data-detail', read_only=True)
#     other = serializers.HyperlinkedRelatedField(many=True, view_name='other-detail', read_only=True)
#     community = serializers.HyperlinkedRelatedField(many=True, view_name='community-detail', read_only=True)
#     professional = serializers.HyperlinkedRelatedField(many=True, view_name='professional-detail', read_only=True)
#     jaega = serializers.HyperlinkedRelatedField(many=True, view_name='jaega-detail', read_only=True)
#
#     class Meta:
#         model = User
#         fields = ['url', 'id', 'username', 'facilty', 'jaega', 'other', 'community', 'professional']






        # 이름
        # 아이디
        # 성별
        # 지역
        # 시구군
        # 비밀번호
        # 선호봉사종류