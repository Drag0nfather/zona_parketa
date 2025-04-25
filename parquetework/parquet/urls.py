from django.conf.urls.static import static
from django.urls import path
from .views import parquet_list, index, about, contact, service, equipment, photos, calculator_submit, calculator
import settings

urlpatterns = [
    path('parquets/', parquet_list, name='parquet_list'),
    path('', index),
    path('index/', index, name='index'),
    path('about/', about),
    path('contact/', contact),
    path('service/', service),
    path('equipment/', equipment),
    path('photos/', photos),
    path('calculator/', calculator, name='calculator'),  # Главная страница калькулятора
    path('calculator/submit/', calculator_submit, name='calculator_submit'),  # Путь для обработки формы
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
