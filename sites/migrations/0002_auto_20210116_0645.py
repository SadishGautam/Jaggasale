# Generated by Django 3.1.1 on 2021-01-16 06:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='title',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='Thesadishgautam@gmail.com', max_length=70),
        ),
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.CharField(default='Tinkune, KTM', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='office_days',
            field=models.CharField(default='Monday – Friday', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='office_time',
            field=models.CharField(default='10:00AM – 6:00PM', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9779812345678'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
