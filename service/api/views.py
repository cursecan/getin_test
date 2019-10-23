from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView,
    UpdateAPIView, DestroyAPIView,
)

from .serializers import (
    PemesananSrializer,
)

from service.models import (
    Pemesanan,
)


class PemesananListApiView(ListAPIView):
    queryset = Pemesanan.objects.all()
    serializer_class = PemesananSrializer


class PemesananDetailApiView(RetrieveAPIView):
    queryset = Pemesanan.objects.all()
    serializer_class = PemesananSrializer

class PemesananCreateApiView(CreateAPIView):
    queryset = Pemesanan.objects.all()
    serializer_class = PemesananSrializer

class PemesananUpdateApiView(UpdateAPIView):
    queryset = Pemesanan.objects.all()
    serializer_class = PemesananSrializer

class PemesananDestroyApiView(DestroyAPIView):
    queryset = Pemesanan.objects.all()
    serializer_class = PemesananSrializer
