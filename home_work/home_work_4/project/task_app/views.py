from django.shortcuts import render
from django.utils import timezone
import logging
import random
from .models import Client, Product
from . import forms

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'task_app/index.html')


def add_product(request):
    """Добавление товара"""
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        message = 'Ошибка данных'
        if form.is_valid():
            image = form.cleaned_data['product_image']
            product_name = form.cleaned_data['product_name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            # работа БД
            logger.debug(f'result: {product_name=}, {description=}, {price=}, {quantity=}')
            product = Product(product_name=product_name,
                              description=description,
                              price=price,
                              quantity=quantity,
                              date_ordered=timezone.now(),
                              product_image=image)
            product.save()
            message = "Товар добавлен !"
            logger.debug(f'PRODUCT SAVE: {product}')
    else:
        form = forms.ProductForm()
        message = "Заполните форму:"
    return render(request, 'task_app/product_add.html', {'form': form, 'message': message, 'title': 'Добавить продукт'})


def update_product(request):
    """Обновление товара"""
    if request.method == 'POST':
        form = forms.ProductUpdateForm(request.POST, request.FILES)
        message = 'Ошибка данных'
        if form.is_valid():
            pk = form.cleaned_data['product_update'].pk
            image = form.cleaned_data['product_image']
            product_name = form.cleaned_data['product_name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            # работа БД
            logger.debug(f'result: {product_name=}, {description=}, {price=}, {quantity=}, {pk=}')
            product_update = Product.objects.filter(pk=pk).first()
            product_update.product_name = product_name
            product_update.description = description
            product_update.price = price
            product_update.quantity = quantity
            product_update.date_ordered = timezone.now()
            product_update.product_image = image
            product_update.save()
            message = "Товар обновлен !"
            logger.debug(f'PRODUCT UPDATE: {product_update}')
    else:
        form = forms.ProductUpdateForm
        message = "Заполните форму для для редактирования товара:"
    return render(request, 'task_app/product_add.html', {'form': form, 'message': message, 'title': 'Обновить продукт'})


def show_products(request):
    products = Product.objects.all()
    return render(request, 'task_app/index.html', {'products': products})


def fake_clients(request, count):
    """ Generate fake clients (arg: count fake clients)"""
    for i in range(count):
        client = Client(name=f'Client #{i + 1}',
                        email=f'Client{i}@mail.com',
                        number_phone=f'+7({i})927654',
                        address=f'address #{i + 1}',
                        registration_date=timezone.now())
        client.save()
    context = {'content': f'Create {count} clients !'}
    logger.debug(f'request: fake_clients, Create {count} clients !')
    return render(request, 'task_app/index.html', context)


def fake_products(request, count):
    """ Generate fake products (arg: count fake products)"""
    for i in range(count):
        product = Product(product_name=f'product #{i + 1}',
                          description=f'description #{i + 1}',
                          price=random.randint(1, 100),
                          quantity=random.randint(10, 100),
                          date_ordered=timezone.now())
        product.save()
    context = {'content': f'Create {count} products !'}
    logger.debug(f'request: fake_products, Create {count} products !')
    return render(request, 'task_app/index.html', context)

# from .models import Client, Product, Order
# def fake_orders(request, pk, count):
#     """ Generate fake orders (arg: pk(id client), count: count products)"""
#     client = Client.objects.filter(pk=pk).first()
#     order = Order(client=client, total_price=0, date_ordered=timezone.now())
#     for i in range(count):
#         product = Product.objects.filter(pk=(i+1)).first()
#         print(product)
#
#         order.total_price += product.price
#         order.save()
#         order.products.add(product)
#     context = {'content': f'Create order: 1-{count} fake products, for client(pk={pk}) ! < {client}'}
#     logger.debug(f'Create order: 1-{count} fake products, for client(pk={pk}) !')
#     return render(request, 'task_app/index.html', context)
