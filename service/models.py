from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from core.models import CommondBase
import uuid

class Pemesanan(CommondBase):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver')
    origin_poin = models.CharField(max_length=100)
    destination_poin = models.CharField(max_length=100)
    order_time = models.DateTimeField(default=timezone.now)
    keterangan = models.CharField(max_length=200, blank=True)
    bayar = models.PositiveIntegerField()

    class Meta:
        ordering = [
            '-id',
        ]