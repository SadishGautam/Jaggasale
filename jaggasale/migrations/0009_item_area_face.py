# Generated by Django 3.1.1 on 2021-04-01 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaggasale', '0008_auto_20210331_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='area_face',
            field=models.CharField(choices=[('E', 'East'), ('W', 'West'), ('N', 'North'), ('S', 'South')], default='North', max_length=2),
            preserve_default=False,
        ),
    ]
