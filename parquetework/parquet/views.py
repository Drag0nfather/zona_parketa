from django.shortcuts import render, redirect
import os
import sys

from .forms.feedback_form import FeedBackForm

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from telegram_stuff.telegram import send_messsage_to_telegram_chat
from .models import ParquetWork, ParquetCategory, ParquetPhoto


def handle_feedback(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone_number')
    message = request.POST.get('description')
    send_messsage_to_telegram_chat(278583648, name, phone, message)
    send_messsage_to_telegram_chat(5414253735, name, phone, message)  # Ромин


def parquet_list(request):
    parquets = ParquetWork.objects.all()
    return render(request, 'parquet_work.html', {'parquets': parquets})


def index(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            handle_feedback(request)
            message = 'Спасибо, что заинтересовались нами! Мы свяжемся с Вами в ближайшее время!'
            photos = ParquetPhoto.objects.all()[:4]
            form = FeedBackForm()
            return render(request, 'index.html', {'photos': photos, 'form': form, 'message': message})
        else:
            message = 'Проверьте правильность введенного телефона'
            photos = ParquetPhoto.objects.all()[:4]
            form = FeedBackForm()
            return render(request, 'index.html', {'photos': photos, 'form': form, 'message': message})
    photos = ParquetPhoto.objects.all()[:4]
    form = FeedBackForm()
    return render(request, 'index.html', {'photos': photos, 'form': form})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            handle_feedback(request)
            message = 'Спасибо, что заинтересовались нами! Мы свяжемся с Вами в ближайшее время!'
            form = FeedBackForm()
            return render(request, 'contact.html', {'form': form, 'message': message})
        else:
            message = 'Проверьте правильность введенного телефона'
            form = FeedBackForm()
            return render(request, 'contact.html', {'form': form, 'message': message})
    form = FeedBackForm()
    return render(request, 'contact.html', {'form': form})


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
