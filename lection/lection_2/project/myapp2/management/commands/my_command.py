from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Hello print'

    def handle(self, *args, **kwargs):
        self.stdout.write('Hello Command !')
