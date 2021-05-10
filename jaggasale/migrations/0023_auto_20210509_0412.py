# Generated by Django 3.1 on 2021-05-09 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jaggasale', '0022_auto_20210508_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('imageitem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jaggasale.item')),
            ],
        ),
        migrations.DeleteModel(
            name='ItemImages',
        ),
    ]
