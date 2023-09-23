from django.core.management.base import BaseCommand
from task2.models import Client, Order, Product


class Command(BaseCommand):
    help = "Generate fake Client and Order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(
                name=f'Name #{i}',
                email=f'mail{i}@mail.ru',
                number_phone=f'+({i})92707585',
                address=f'address #{i}'
            )
            client.save()
            for j in range(1, count + 1):
                product = Product.objects.filter(pk=i)
                print(product)
                print(product)
                order = Order(
                    client=client,
                    total_price=99.9+i
                )
                order.save()
        print(f'Success, {count} entries')
