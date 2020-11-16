# Generated by Django 3.1.3 on 2020-11-14 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heads', '0006_auto_20201114_0232'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('husband_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('customer_type', models.CharField(choices=[('I', 'Individual'), ('A', 'Artificial Person')], max_length=1)),
                ('residential_address1', models.CharField(blank=True, max_length=25, null=True)),
                ('residential_address2', models.CharField(blank=True, max_length=25, null=True)),
                ('residential_address3', models.CharField(blank=True, max_length=25, null=True)),
                ('residential_address4', models.CharField(blank=True, max_length=25, null=True)),
                ('residential_address5', models.CharField(blank=True, max_length=25, null=True)),
                ('city', models.CharField(blank=True, max_length=26, null=True)),
                ('state_code', models.IntegerField(blank=True, null=True)),
                ('state_name', models.CharField(blank=True, max_length=25, null=True)),
                ('country_code', models.IntegerField(blank=True, null=True)),
                ('country_name', models.CharField(blank=True, max_length=25, null=True)),
                ('pan_number', models.CharField(max_length=10)),
                ('voter_card', models.CharField(blank=True, max_length=16, null=True)),
                ('driving_licence', models.CharField(blank=True, max_length=16, null=True)),
                ('ration_card', models.CharField(blank=True, max_length=16, null=True)),
                ('adhar_number', models.CharField(blank=True, max_length=16, null=True)),
                ('mobile_number1', models.CharField(max_length=10)),
                ('mobile_number2', models.CharField(blank=True, max_length=10, null=True)),
                ('phone_home', models.CharField(blank=True, max_length=10, null=True)),
                ('phone_office', models.CharField(blank=True, max_length=10, null=True)),
                ('office_address1', models.CharField(blank=True, max_length=25, null=True)),
                ('office_address2', models.CharField(blank=True, max_length=25, null=True)),
                ('office_address3', models.CharField(blank=True, max_length=25, null=True)),
                ('office_address4', models.CharField(blank=True, max_length=25, null=True)),
                ('office_address5', models.CharField(blank=True, max_length=25, null=True)),
                ('office_city', models.CharField(blank=True, max_length=26, null=True)),
                ('office_state_code', models.IntegerField(blank=True, null=True)),
                ('office_state_name', models.CharField(blank=True, max_length=25, null=True)),
                ('office_country_code', models.IntegerField(blank=True, null=True)),
                ('office_country_name', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='customer_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='heads.customerid'),
            preserve_default=False,
        ),
    ]