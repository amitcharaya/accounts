# Generated by Django 3.1.3 on 2020-11-14 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heads', '0024_auto_20201114_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='narration',
            field=models.CharField(default='old txns', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('IN', 'Interest'), ('LD', 'Loan Disbursement'), ('CW', 'Cash Withdrwal'), ('EM', 'EMI Payments'), ('DP', 'Cash Deposit')], default='NA', max_length=2),
            preserve_default=False,
        ),
    ]