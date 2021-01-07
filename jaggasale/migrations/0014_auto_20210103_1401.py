# Generated by Django 3.1.1 on 2021-01-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaggasale', '0013_auto_20210101_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=2),
        ),
    ]
