# Generated by Django 2.2.3 on 2019-07-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20190726_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='line_id',
            field=models.CharField(max_length=50),
        ),
    ]