# Generated by Django 2.2.3 on 2019-08-04 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='district',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='finalPrice',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='grand_total',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='increment_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='productName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='provice',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='qty',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_amount',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='subtotal',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='weight',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
