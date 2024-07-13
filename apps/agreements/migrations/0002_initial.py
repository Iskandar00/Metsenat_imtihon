# Generated by Django 5.0.7 on 2024-07-11 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agreements', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.sponsor'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.student'),
        ),
    ]
