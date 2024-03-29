from django.db import models


class ParquetCategory(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name = 'Категория работ'
        verbose_name_plural = 'Категории работ'

    def __str__(self):
        return self.category_name


class ParquetWork(models.Model):
    category = models.ForeignKey(to=ParquetCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.name


class ParquetPhoto(models.Model):
    name = models.CharField(blank=True, max_length=100)
    photo = models.ImageField()

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.name or str(self.id)
