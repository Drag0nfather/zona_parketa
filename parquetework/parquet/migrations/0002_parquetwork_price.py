# Generated by Django 4.1.6 on 2023-02-13 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parquet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parquetwork',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]