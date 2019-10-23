from rest_framework.generics import (
    ListAPIView, CreateAPIView, 
    RetrieveAPIView, UpdateAPIView, DestroyAPIView,
)

from .serializers import (
    CustomerSerializer, DriverSerializer
)
from userprofile.models import UserProfile


class CustomerListApiView(ListAPIView):
    queryset = UserProfile.objects.filter(is_driver=False)
    serializer_class = CustomerSerializer

class CustomerCreateApiView(CreateAPIView):
    model = UserProfile
    serializer_class = CustomerSerializer

class CustomerDetailApiView(RetrieveAPIView):
    queryset = UserProfile.objects.filter(is_driver=False)
    serializer_class = CustomerSerializer

class CustomerUpdateApiView(UpdateAPIView):
    queryset = UserProfile.objects.filter(is_driver=False)
    serializer_class = CustomerSerializer

class CustomerDestroyApiView(DestroyAPIView):
    queryset = UserProfile.objects.filter(is_driver=False)
    serializer_class = CustomerSerializer


class DriverListApiView(ListAPIView):
    queryset = UserProfile.objects.filter(is_driver=True)
    serializer_class = DriverSerializer

class DriverCreateApiView(CreateAPIView):
    model = UserProfile
    serializer_class = DriverSerializer

class DriverDetailApiView(RetrieveAPIView):
    queryset = UserProfile.objects.filter(is_driver=True)
    serializer_class = DriverSerializer

class DriverUpdateApiView(UpdateAPIView):
    queryset = UserProfile.objects.filter(is_driver=True)
    serializer_class = DriverSerializer

class DriverDestroyApiView(DestroyAPIView):
    queryset = UserProfile.objects.filter(is_driver=True)
    serializer_class = DriverSerializer
