# Generated by Django 3.1.3 on 2020-11-14 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heads', '0010_auto_20201114_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='interest_credit_applicable',
            field=models.CharField(blank=True, choices=[('Y', 'YES'), ('N', 'NO')], max_length=1),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='interest_debit_applicable',
            field=models.CharField(blank=True, choices=[('Y', 'YES'), ('N', 'NO')], max_length=1),
        ),
    ]
