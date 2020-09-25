from django.shortcuts import render


# Create your views here.
def index (request):
    context = {
        'page_title' : 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def contact (request):
    context = {
        'page_title': 'контакты',
    }
    return render(request, 'mainapp/contact.html', context)


def products (request):
    context = {
        'page_title': 'каталог',
    }
    return render(request, 'mainapp/products.html', context)

