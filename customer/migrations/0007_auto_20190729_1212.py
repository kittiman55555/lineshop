# Generated by Django 2.2.3 on 2019-07-29 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20190729_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_img',
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name_line',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
