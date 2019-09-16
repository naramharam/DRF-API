from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from data.models import Facility, Other, Community, Jaega, Professional, All, UserModel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = '__all__'


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Facility
        fields = ['url', 'id', 'owner', 'title', 'location', 'sub_location', 'gender', 'contents']


class OtherSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Other
        fields = ['url', 'id', 'owner', 'title', 'location', 'sub_location', 'gender', 'contents']


class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Community
        fields = ['url', 'id', 'owner', 'title', 'location', 'sub_location', 'gender', 'contents']


class JaeGaSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Jaega
        fields = ['url', 'id', 'owner', 'title', 'location', 'sub_location', 'gender', 'contents']


class ProfessionalSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Professional
        fields = ['url', 'id', 'owner', 'title', 'location', 'sub_location', 'gender', 'contents']


class AllSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = All
        fields = ['url', 'id', 'owner', 'title', 'location', 'sub_location', 'gender', 'contents']



# class LoginSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = LoginUserModel
#         fields = '__all__'
