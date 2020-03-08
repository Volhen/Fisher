from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import ProductCategory, Product
from django.urls import reverse


def index(request):

    context = {
        "page_title": 'Главная',
    }

    return render(request, 'mainapp/index.html', context)


def contacts(request):

    context = {
        "page_title": 'Контакты',
    }

    return render(request, 'mainapp/contacts.html', context)


def catalog(request):

    links_menu = ProductCategory.objects.all()
    products = Product.objects.all().order_by('price')

    context = {
        'page_title': 'Каталог',
        'products': products,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/catalog.html', context)


def blog(request):

    context = {
        "page_title": 'Блог',
    }

    return render(request, 'mainapp/blog.html', context)


def about(request):

    context = {
        "page_title": 'О нас',
    }

    return render(request, 'mainapp/about.html', context)