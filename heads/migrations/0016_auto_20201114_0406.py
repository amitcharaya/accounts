# Generated by Django 3.1.3 on 2020-11-14 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heads', '0015_auto_20201114_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='credit_interest_account',
            field=models.CharField(blank=True, choices=[('S', 'Same Account'), ('O', 'Other Account')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='interest_credit_table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditinterst_table', to='heads.interesttable'),
        ),
    ]
