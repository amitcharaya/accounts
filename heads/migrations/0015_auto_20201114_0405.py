# Generated by Django 3.1.3 on 2020-11-14 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heads', '0014_auto_20201114_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='credit_interest_account',
            field=models.CharField(blank=True, choices=[('S', 'Same Account'), ('O', 'Other Account')], max_length=1),
        ),
    ]