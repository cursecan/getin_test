from rest_framework import serializers
from django.contrib.auth.models import User

from service.models import (
    Pemesanan,
)

from userprofile.api.serializers import (
    SimpleUserSerializer,
)

class PemesananUserSerializer(serializers.Serializer):
    customer_uid = serializers.UUIDField(write_only=True)
    driver_uid = serializers.UUIDField(write_only=True)    

    def validate(self, attrs):
        customer_uid = attrs.get('customer_uid')
        driver_uid = attrs.get('driver_uid')

        if not User.objects.filter(userprofile__uid=customer_uid, userprofile__is_driver=False).exists():
            raise serializers.ValidationError({
                'customer_id': 'User customer not found.'
            })

        if not User.objects.filter(userprofile__uid=driver_uid, userprofile__is_driver=True).exists():
            raise serializers.ValidationError({
                'driver_id': 'User driver not found.'
            })

        return attrs


class PemesananSrializer(PemesananUserSerializer, serializers.ModelSerializer):
    customer = SimpleUserSerializer(read_only=True)
    driver = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Pemesanan
        fields = [
            'id', 'uid',
            'customer_uid', 'driver_uid',
            'customer', 'driver',
            'origin_poin', 'destination_poin',
            'order_time', 'keterangan', 'bayar'
        ]

        read_only_fields = [
            'id', 'uid', 'order_time',
        ]

    def create(self, validated_data):
        customer = User.objects.get(userprofile__uid=validated_data.get('customer_uid'))
        driver = User.objects.get(userprofile__uid=validated_data.get('driver_uid'))
    
        obj = Pemesanan.objects.create(
            customer=customer, driver=driver,
            origin_poin = validated_data.get('origin_poin'),
            destination_poin = validated_data.get('destination_poin'),
            keterangan = validated_data.get('keterangan'),
            bayar = validated_data.get('bayar'),
        )
        return obj

    def update(self, instance, validated_data):
        customer = User.objects.get(userprofile__uid=validated_data.get('customer_uid'))
        driver = User.objects.get(userprofile__uid=validated_data.get('driver_uid'))

        instance.origin_poin = validated_data.get('origin_poin', instance.origin_poin)
        instance.destination_poin = validated_data.get('destination_poin', instance.destination_poin)
        instance.bayar = validated_data.get('bayar', instance.bayar)

        return instance