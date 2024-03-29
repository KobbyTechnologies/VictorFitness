# Generated by Django 4.0.4 on 2023-03-06 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_transaction_delete_initiate'),
    ]

    operations = [
        migrations.CreateModel(
            name='LipaNaMpesaOnline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckoutRequestID', models.CharField(blank=True, max_length=50, null=True)),
                ('MerchantRequestID', models.CharField(blank=True, max_length=20, null=True)),
                ('ResultCode', models.IntegerField(blank=True, null=True)),
                ('ResultDesc', models.CharField(blank=True, max_length=120, null=True)),
                ('Amount', models.FloatField(blank=True, null=True)),
                ('MpesaReceiptNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('TransactionDate', models.DateTimeField(blank=True, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
