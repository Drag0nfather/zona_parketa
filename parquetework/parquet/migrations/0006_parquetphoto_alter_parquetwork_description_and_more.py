# Generated by Django 4.1.6 on 2023-03-20 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parquet', '0005_parquetcategory_remove_parquetwork_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParquetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='parquetwork',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='parquetwork',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]