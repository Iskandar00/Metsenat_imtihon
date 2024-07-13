# Generated by Django 5.0.7 on 2024-07-11 07:56

import apps.users.validate
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agreements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_type', models.CharField(choices=[('Yuridik', 'Yuridik'), ('Jismoniy', 'Jismoniy')], max_length=10)),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=13, validators=[apps.users.validate.phone_number_validate])),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('company_name', models.CharField(blank=True, max_length=250)),
                ('payment_type', models.CharField(choices=[('Naqd', 'Naqd'), ('Online', 'Online')], max_length=10)),
                ('status', models.CharField(choices=[('Yangi', 'Yangi'), ('Moderatsiyada', 'Moderatsiyada'), ('Tasdiqlangan', 'Tasdiqlangan'), ('Bekor qilingan', 'Bekor Qilingan')], default='Yangi', max_length=50)),
                ('spand_amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=13, validators=[apps.users.validate.phone_number_validate])),
                ('level', models.CharField(choices=[('Magiter', 'Magister'), ('Bakalavr', 'Bakalavr')], max_length=10)),
                ('contract', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('sponsored_amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('place_of_study', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agreements.placeofstudy')),
            ],
        ),
    ]
