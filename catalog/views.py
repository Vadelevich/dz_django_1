from django.shortcuts import render

from catalog.models import Product, Category


def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    contex = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', contex)


def gallery(request):
    contex = {
        'object_list' : Product.objects.all(),
    }
    return render(request,'catalog/gallery.html',contex)
