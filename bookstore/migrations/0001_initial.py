# Generated by Django 3.2 on 2022-02-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('uid', models.CharField(editable=False, max_length=32)),
                ('plan', models.CharField(editable=False, max_length=32)),
                ('marchantPaymentId', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'paymeny_history',
                'verbose_name_plural': 'payment_histories',
            },
        ),
    ]
