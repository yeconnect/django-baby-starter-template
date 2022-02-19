from django.urls import path

from . import views

app_name = 'bookstore'

urlpatterns = [
    path('checkout', views.index, name='支払い前の画面'),
    path('create-checkout-session',
         views.redirect_to_paypay, name='支払い画面にリダイレクトする'),
    path('get-user-from-paymentid',
         views.get_user_from_paymentID, name='決済IDを元にユーザ情報を返す'),
    path('generate-qr-code', views.generate_qr_code, name='QRコードを作成する'),
    path('success', views.success, name='success'),
]
