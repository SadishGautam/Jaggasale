# Generated by Django 3.1.1 on 2021-02-05 06:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaggasale', '0016_item_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='owner_name',
            field=models.CharField(default='owner', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='phone_number',
            field=models.CharField(default='+977 9845900495', max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9779812345678'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
