from django.shortcuts import render

from telegram_stuff.telegram import send_messsage_to_telegram_chat
from .models import ParquetWork, ParquetCategory, ParquetPhoto


def handle_feedback(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    send_messsage_to_telegram_chat(278583648, name, phone, message)
    # send_messsage_to_telegram_chat(5414253735, name, phone, message)   Ромин


def parquet_list(request):
    parquets = ParquetWork.objects.all()
    return render(request, 'parquet_work.html', {'parquets': parquets})


def index(request):
    if request.method == 'POST':
        handle_feedback(request)
        photos = ParquetPhoto.objects.all()[:4]
        return render(request, 'index.html', {'photos': photos})
    photos = ParquetPhoto.objects.all()[:4]
    return render(request, 'index.html', {'photos': photos})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        handle_feedback(request)
        return render(request, 'contact.html')
    return render(request, 'contact.html')


def service(request):
    categories = ParquetCategory.objects.all()
    selected_category = None
    parquet_works = None
    category_id = request.GET.get('category_id')
    if category_id:
        selected_category = ParquetCategory.objects.get(id=category_id)
        parquet_works = ParquetWork.objects.filter(category=selected_category)
    else:
        selected_category = ParquetCategory.objects.get(id=1)
        parquet_works = ParquetWork.objects.filter(category=selected_category)
    context = {
        'categories': categories,
        'selected_category': selected_category,
        'parquet_works': parquet_works,
    }

    return render(request, 'service.html', context)


def equipment(request):
    return render(request, 'equipment.html')


def photos(request):
    photos = ParquetPhoto.objects.all()
    return render(request, 'photos.html', {'photos': photos})
