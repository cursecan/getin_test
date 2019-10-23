from rest_framework import serializers
from django.contrib.auth.models import User

from userprofile.models import UserProfile

class SimpleUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'first_name', 'last_name',
        ]


class CustomerSignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(username=email).exists():

            raise serializers.ValidationError({
                'username': 'This username is already taken.'
            })
        return attrs


class CustomerSerializer(CustomerSignUpSerializer, serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'id', 'uid', 'gender', 'user',
            'first_name', 'last_name', 'email', 'password',
        ]
        read_only_fields = ['id', 'uid'] 


    def create(self, validated_data):
        email = validated_data.get('email')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )

        user.refresh_from_db()
        user.userprofile.gender = validated_data.get('gender')
        user.userprofile.save()

        return user.userprofile

    def update(self, instance, validated_data):
        instance.gender = validated_data.get('gender', instance.gender)

        user = instance.user
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.email = validated_data.get('email', user.email)
        user.username = validated_data.get('email', user.username)
        user.save()

        return instance


class DriverSignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    no_kendaraan = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(username=email).exists():

            raise serializers.ValidationError({
                'username': 'This username is already taken.'
            })
        return attrs


class DriverSerializer(DriverSignUpSerializer, serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'id', 'uid', 'gender', 'user',
            'first_name', 'last_name', 'email', 'no_kendaraan', 'password',
        ]
        read_only_fields = ['id', 'uid'] 


    def create(self, validated_data):
        email = validated_data.get('email')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )

        user.refresh_from_db()
        user.userprofile.gender = validated_data.get('gender')
        user.userprofile.no_kendaraan = validated_data.get('no_kendaraan')
        user.userprofile.is_driver = True
        user.userprofile.save()

        return user.userprofile

    def update(self, instance, validated_data):
        instance.gender = validated_data.get('gender', instance.gender)
        instance.no_kendaraan = validated_data('no_kendaraan', instance.no_kendaraan)

        user = instance.user
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.email = validated_data.get('email', user.email)
        user.username = validated_data.get('email', user.username)
        user.save()

        return instance