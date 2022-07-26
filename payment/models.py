from django.db import models
from datetime import datetime
from django.utils import timezone
import pytz

from django.conf import settings

from landing.models import Program_Detail

# Create your models here.


class Initiate(models.Model):
    CheckoutRequestID = models.CharField(max_length=50, null=True, unique=True)
    MerchantRequestID = models.CharField(max_length=30, null=True, unique=True)
    ResultCode = models.IntegerField(null=True)
    mode = models.CharField(max_length=40, null=True, blank=True)
    ResultDescription = models.TextField(max_length=200, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, related_name="initiated")
    service = models.ForeignKey(Program_Detail, on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.CheckoutRequestID

    class Meta:
        verbose_name_plural = "Initiated Transactions"
        verbose_name = "Initiated Transaction"
