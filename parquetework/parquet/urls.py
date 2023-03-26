from django.conf.urls.static import static
from django.urls import path
from .views import parquet_list, index, about, contact, service, equipment, photos
import settings

urlpatterns = [
    path('parquets/', parquet_list, name='parquet_list'),
    path('', index),
    path('index/', index),
    path('about/', about),
    path('contact/', contact),
    path('service/', service),
    path('equipment/', equipment),
    path('photos/', photos)
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
