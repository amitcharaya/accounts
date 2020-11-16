# Generated by Django 3.1.3 on 2020-11-13 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountheads',
            name='classification',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='heads.accountheads'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accountheads',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
