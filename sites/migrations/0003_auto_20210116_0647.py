# Generated by Django 3.1.1 on 2021-01-16 06:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_auto_20210116_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default='+977 9845900495', max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9779812345678'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
