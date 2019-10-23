from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from core.models import CommondBase

import uuid

class UserProfile(CommondBase):
    PRIA = 'P'
    WANITA = 'W'
    GENDER_LIST = (
        (PRIA, 'Pria'),
        (WANITA, 'Wanita'),
    )
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    no_telp = models.CharField(max_length=16, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_LIST, default=PRIA)
    is_driver = models.BooleanField(default=False)
    no_kendaraan = models.CharField(max_length=15, blank=True)

    class Meta:
        ordering = [
            '-id'
        ]