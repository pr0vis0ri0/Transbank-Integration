from django.shortcuts import render
from .jsonresponse import JSONResponse
from rest_framework.views import APIView
from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    return render(request,'prueba.html')

def header_request_transbank() :
    headers = {
        "Authorization": "Token",
        "Tbk-Api-Key-Id": "597055555532",
        "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        'Referrer-Policy': 'origin-when-cross-origin',
        } 
    return headers

class TransbankCreate(APIView):
    def post(self, request):
        headers = header_request_transbank()
        data = request.data
        url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"
        response = requests.post(url, json=data, headers=headers)
        return JSONResponse(response)

class TransbankCommit(APIView):
    def put(self, request, tokenws):
        headers = header_request_transbank()
        url = f"https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{tokenws}"
        response = requests.put(url, headers=headers)
        return JSONResponse(response)

class TransbankReverseOrCancel(APIView):
    def post(self, request, tokenws):
        headers = header_request_transbank()
        data = request.data
        url = f"https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{tokenws}/refunds"
        response = requests.post(url, json=data, headers=headers)
        return JSONResponse(response)