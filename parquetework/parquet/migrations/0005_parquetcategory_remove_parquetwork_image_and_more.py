# Generated by Django 4.1.6 on 2023-02-16 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parquet', '0004_alter_parquetwork_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParquetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='parquetwork',
            name='image',
        ),
        migrations.AddField(
            model_name='parquetwork',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parquet.parquetcategory'),
            preserve_default=False,
        ),
    ]