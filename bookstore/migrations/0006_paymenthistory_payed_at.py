# Generated by Django 3.2 on 2022-02-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_auto_20220219_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenthistory',
            name='payed_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='決済完了時刻'),
        ),
    ]
