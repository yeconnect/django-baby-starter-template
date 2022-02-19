from django.db import models

# 決済履歴データベース: 親のユーザID, プランの種類, 決済IDを紐付け
# プランは後から追加可能に


class Plan(models.Model):
    plan_name = models.CharField(max_length=32, verbose_name="プランの種類")

    def __str__(self):
        return self.plan_name

    class Meta:
        verbose_name = 'プランの種類'
        verbose_name_plural = 'プランの種類'


class PaymentHistory(models.Model):
    uid = models.CharField(max_length=32, verbose_name="ユーザID")
    plan = models.ForeignKey(
        Plan, on_delete=models.PROTECT, verbose_name="プランの種類")
    paymentID = models.CharField(
        max_length=32, primary_key=True, verbose_name="決済ID")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="決済画面移動時刻")
    payed_at = models.DateTimeField(
        null=True, blank=True, verbose_name="決済完了時刻")

    def __str__(self):
        return self.paymentID

    class Meta:
        verbose_name = '決済履歴'
        verbose_name_plural = '決済履歴'
