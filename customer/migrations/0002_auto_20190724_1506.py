# Generated by Django 2.2.3 on 2019-07-24 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='store_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]