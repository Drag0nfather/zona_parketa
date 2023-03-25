from django.contrib import admin
from .models import ParquetWork, ParquetCategory, ParquetPhoto

admin.site.register(ParquetCategory)
admin.site.register(ParquetWork)
admin.site.register(ParquetPhoto)
