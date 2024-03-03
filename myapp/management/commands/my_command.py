from django.core.management.base import BaseCommand
from myapp.models import Autor


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(1, 10):
            author = Autor(name=f'name{i}',
                           surname=f'surname{i}',
                           email=f'email{i}',
                           biography=f'biography{i}',
                           birthday=f'2000-01-0{i}')
            author.save()
