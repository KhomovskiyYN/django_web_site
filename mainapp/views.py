from django.shortcuts import render
from datetime import datetime


# Create your views here.
def index (request):
    context = {
        'page_title' : 'главная',
        #'datetime': datetime.now(),
    }
    return render(request, 'mainapp/index.html', context)


def products (request):
    context = {
        'page_title': 'каталог',
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-999-888-77-77',
            'email': 'info@homkashop.ru',
            'address': 'В пределах МКАД',

        },
        {
            'city': 'Санкт-Петербург',
            'phone': '+7-777-888-99-99',
            'email': 'info@homkashop.ru',
            'address': 'В пределах КАД',

        },
    ]

    context = {
        'page_title': 'контакты',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)