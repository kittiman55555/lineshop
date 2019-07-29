# Generated by Django 2.2.3 on 2019-07-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('store_id', models.IntegerField(default=0)),
                ('line_id', models.CharField(max_length=50)),
                ('profile_img', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]