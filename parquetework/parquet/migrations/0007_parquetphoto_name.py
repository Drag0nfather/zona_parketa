# Generated by Django 4.1.6 on 2023-03-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parquet', '0006_parquetphoto_alter_parquetwork_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parquetphoto',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
