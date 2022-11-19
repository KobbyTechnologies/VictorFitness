from django.shortcuts import render
from .serializers import LipaNaMpesaSerializer
from rest_framework.generics import CreateAPIView
from payment.models import LipaNaMpesaOnline
from rest_framework.permissions import AllowAny

from datetime import datetime
import pytz
from rest_framework.response import Response



class LipaNaMpesaAPIView(CreateAPIView):
    queryset = LipaNaMpesaOnline.objects.all()
    serializer_class = LipaNaMpesaSerializer
    permission_classes = AllowAny

    def create(self, request):
        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        result_code = request.data["Body"]["stkCallback"]["ResultCode"]
        result_description = request.data["Body"]["stkCallback"]["ResultDesc"]
        amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]["Value"]
        mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"]
        transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]["Value"]
        phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"]

        str_transaction_date = str(transaction_date)

        transaction_datetime = datetime.strptime(str_transaction_date, "%Y%m%d%H%M%S")

        aware_transaction_datetime = pytz.utc.localize(transaction_datetime)

        our_model = LipaNaMpesaOnline.objects.create(
            CheckoutRequestID=checkout_request_id,
            MerchantRequestID=merchant_request_id,
            Amount=amount,
            ResultCode=result_code,
            ResultDesc=result_description,
            MpesaReceiptNumber=mpesa_receipt_number,
            TransactionDate=aware_transaction_datetime,
            PhoneNumber=phone_number,
        )

        our_model.save()
        return Response({"OurResultDesc": "YEEY!!! It worked!"})