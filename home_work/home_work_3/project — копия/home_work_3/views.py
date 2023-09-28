from django.shortcuts import render
import logging

from django.core.management.base import BaseCommand
import random
from django.utils import timezone

from models import Client, Product, Order

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('request index')
    return render(request, 'home_work_3/index.html')


class Command(BaseCommand):
    help = 'Generate fake DB'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count client, orders and product')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for j in range(1, count + 1):
            product = Product(product_name=f'product #{j}',
                              description=f'description #{j}',
                              price=random.randint(1, 100),
                              quantity=random.randint(10, 100),
                              date_ordered=timezone.now())
            product.save()
        for i in range(1, count + 1):
            client = Client(name=f'Client #{i}',
                            email=f'Client{i}@mail.com',
                            number_phone=f'+7({i})927654',
                            address=f'address #{i}',
                            registration_date=timezone.now())
            client.save()
        for _ in range(1, count + 1):
            client = Client.objects.order_by('?').first()
            for _ in range(1, random.randint(1, count)):
                total_price = 0
                order = Order(customer=client, date_ordered=timezone.now())
                for _ in range(1, random.randint(1, count)):
                    product = Product.objects.order_by('?').first()
                    total_price += product.price
                    order.total_price = total_price
                    order.save()
                    order.products.add(product)
