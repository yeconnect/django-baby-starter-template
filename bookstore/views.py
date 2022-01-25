from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

import stripe

stripe.api_key = 'sk_test_51KLfVvIhiJe7aSQz2NstPAOrSZhUxGi9AUAXWxDE7p4r8NrmaxoXkbN0G37F3bT7lvxwphC8fOKCTNNkGbTrByZS00SixCsT36'


def checkout(request):
    return render(request,"checkout.html")

def success(request):
    return render(request,"success.html")

def cancel(request):
    return render(request,"cancel.html")

class HttpResponseSeeOther(HttpResponseRedirect):
    """ 303でリダイレクトさせる(Stripe公式のFlaskの実装が303だったため) """
    status_code = 303

@csrf_exempt
def create_checkout_session(request):
    MY_DOMAIN = f'{request.scheme}://{request.get_host()}'
    print(MY_DOMAIN)
    PRICE_ID = "price_1KLfXrIhiJe7aSQzPpmkpei0"
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': PRICE_ID,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url = MY_DOMAIN + '/success',
            cancel_url = MY_DOMAIN + '/cancel',
        )
        return HttpResponseSeeOther(checkout_session.url)
    except Exception as e:
        print(str(e))
        # ここハンドリング