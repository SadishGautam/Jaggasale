# Generated by Django 3.1.1 on 2021-03-21 14:31

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('category', models.CharField(choices=[('H', 'House'), ('A', 'Apartment'), ('L', 'Land')], default='Error fetching category', max_length=2)),
                ('label', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=2)),
                ('sold_or_rent', models.CharField(choices=[('sold', 'SOLD'), ('rent', 'RENT')], default='SOLD', max_length=4)),
                ('picture_count', models.IntegerField(blank=True, null=True)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('owner_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(default='', max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9779812345678'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('rooms', models.IntegerField(blank=True, null=True)),
                ('bathrooms', models.IntegerField(blank=True, null=True)),
                ('floors', models.IntegerField(blank=True, null=True)),
                ('Description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('location', models.CharField(choices=[('K', 'Kathmandu'), ('L', 'Lalitpur'), ('L', 'Bhaktapur'), ('C', 'Chitwan')], max_length=2)),
                ('map', models.CharField(blank=True, max_length=150, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('have_parking', models.BooleanField(default=False, verbose_name='Parking')),
                ('have_garden', models.BooleanField(default=False, verbose_name='garden')),
                ('have_drinage', models.BooleanField(default=False, verbose_name='drinage')),
                ('have_balcony', models.BooleanField(default=False, verbose_name='balcony')),
                ('have_hallRoom', models.BooleanField(default=False, verbose_name='hallRoom')),
                ('have_diningRoom', models.BooleanField(default=False, verbose_name='diningRoom')),
                ('have_elevator', models.BooleanField(default=False, verbose_name='elevator')),
                ('have_water', models.BooleanField(default=False, verbose_name='water')),
                ('have_electricityBackup', models.BooleanField(default=False, verbose_name='electricityBackup')),
                ('have_securityStaff', models.BooleanField(default=False, verbose_name='securityStaff')),
                ('have_lift', models.BooleanField(default=False, verbose_name='lift')),
                ('have_kidsPlayground', models.BooleanField(default=False, verbose_name='kidsPlayground')),
                ('have_electricityPole', models.BooleanField(default=False, verbose_name='electricityPole')),
                ('have_road', models.BooleanField(default=False, verbose_name='road')),
                ('have_waterSupply', models.BooleanField(default=False, verbose_name='waterSupply')),
                ('image', models.ImageField(upload_to='static/images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('images', models.ImageField(blank=True, upload_to='static/images')),
                ('imageitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jaggasale.item')),
            ],
        ),
    ]
