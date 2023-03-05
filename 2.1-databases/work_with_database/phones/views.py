from django.http import HttpRequest
from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    print(sort)
    if sort == None:
        context = {
            'phones': Phone.objects.all()}
    elif sort in 'name':
        context = {'phones':Phone.objects.all().order_by(
            'name')}
    elif sort in 'min_price':
        context = {'phones':Phone.objects.all().order_by(
            'price')}
    elif sort in 'max_price':
        context = {'phones':Phone.objects.all().order_by(
            'price').reverse()}
    else:
        context = {
            'phones': Phone.objects.all()}
    return render(request, template, context)

def show_product(request, slug):
    print('hello')
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)

