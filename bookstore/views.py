from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
import paypayopa

from PIL import Image
import qrcode
import base64
from io import BytesIO
import uuid

from .models import PaymentHistory, Plan

API_KEY = "a_rMJ9p06Bc1_5dse"
API_SECRET = "8F1h8BAk2eiIj5DqQ5oVbiqOQywYCHu74+Nd1dLPQfo="
MERCHANT_ID = "469444504158363648"

client = paypayopa.Client(auth=(API_KEY, API_SECRET), production_mode=False)
client.set_assume_merchant(MERCHANT_ID)


def index(request):
    return render(request, "checkout.html")


@csrf_exempt
def redirect_to_paypay(request):
    # ↓本来は引数から受け取る
    uid = "UboZTQTtbxdn7D9vjnl01iLRsck2"
    plan = "UT"
    # ↑
    paymentID = str(uuid.uuid4().hex)
    PaymentHistory.objects.create(uid=uid, plan=Plan.objects.get(
        plan_name=plan), paymentID=paymentID)
    req = {
        "merchantPaymentId": paymentID,
        "codeType": "ORDER_QR",
        "redirectUrl": "http://localhost:4989/success",
        "redirectType": "WEB_LINK",
        "orderDescription": "Example - Mune Cake shop",
        "orderItems": [{
            "name": "Moon cake",
            "category": "pasteries",
            "quantity": 1,
            "productID": "67678",
            "unitPrice": {
                "amount": 1,
                "currency": "JPY"
            }
        }],
        "amount": {
            "amount": 22980,
            "currency": "JPY"
        },
    }
    # Calling the method to create a qr code
    response = client.Code.create_qr_code(req)
    # Printing if the method call was SUCCESS
    print(response['resultInfo']['code'])
    paypay_url = response['data']['url']
    print(paypay_url)
    return redirect(paypay_url)


def get_user_from_paymentID(request):
    user = PaymentHistory.objects.get(
        paymentID=request.data.paymentID)
    return ({
        'uid': user.uid,
        'plan': user.plan.plan_name
    })


def success(request):
    return render(request, "success.html")


@csrf_exempt
def generate_qr_code(request):
    req = {
        "paymentID": "dfasfasfdasdfadfasdfdasdfdddfas",
        "codeType": "ORDER_QR",
        "redirectUrl": "http://foobar.com",
        "redirectType": "WEB_LINK",
        "orderDescription": "Example - Mune Cake shop",
        "orderItems": [{
            "name": "Moon cake",
            "category": "pasteries",
            "quantity": 1,
            "productID": "67678",
            "unitPrice": {
                "amount": 1,
                "currency": "JPY"
            }
        }],
        "amount": {
            "amount": 10000,
            "currency": "JPY"
        },
    }
    response = client.Code.create_qr_code(req)
    img = qrcode.make(response['data']['url'])
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr = base64.b64encode(buffer.getvalue()).decode().replace("'", "")
    param = {'qr': qr}
    return render(request, "qr.html", param)
