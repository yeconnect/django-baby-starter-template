import stripe
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = 'あなたの秘密鍵'


def checkout(request):
    return render(request, "checkout.html")


def success(request):
    return render(request, "success.html")


def cancel(request):
    return render(request, "cancel.html")


@csrf_exempt
def create_checkout_session(request):
    MY_DOMAIN = f'{request.scheme}://{request.get_host()}'
    PRICE_ID = "あなたの値段ID"
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': PRICE_ID,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=MY_DOMAIN +
            '/bookstore/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=MY_DOMAIN + '/bookstore/cancel',

            # これは任意 (メタデータの追加指定ができる)
            payment_intent_data={
                "metadata": {
                    "user_hogehoge": "Django Baby",
                }
            }
        )
        print("決済ページのURLはこれ →" + checkout_session.url)
        return redirect(checkout_session.url)
    except Exception as e:
        print("エラー内容："+str(e))
        # ここもう少しハンドリングするべき


endpoint_secret = 'whsec_あなたの文字列'


@csrf_exempt
def handle_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        # Stripeが送ってきたものか判定
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        # Payloadが変な時
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Stripeでない第三者が不正に送ってきた時
        return HttpResponse(status=400)

    # eventのtypeによって、好きなように分岐
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        metadata = payment_intent["metadata"]
        print('決済が完了したのでここで決済処理をします！！！')
        print("決済の詳細情報→" + str(payment_intent))
        print("指定したメタデータの取り出し→" + str(metadata))

    else:
        event_type = event['type']
        print(f'Event type {event_type}')
    return HttpResponse(status=200)
