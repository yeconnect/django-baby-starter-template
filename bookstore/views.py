import stripe
from django.http import HttpResponseRedirect
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
            success_url=MY_DOMAIN + '/bookstore/success',
            cancel_url=MY_DOMAIN + '/bookstore/cancel',
        )
        return redirect(checkout_session.url)
    except Exception as e:
        print(str(e))
        # ここもう少しハンドリングするべき
