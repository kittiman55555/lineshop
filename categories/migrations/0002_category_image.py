# Generated by Django 2.2.3 on 2019-08-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/%Y/%m/%d/'),
        ),
    ]