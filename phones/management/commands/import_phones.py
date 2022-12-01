import csv
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone1 in phones:
            Phone.objects.create(name=phone1['name'], price=phone1['price'], image=phone1['image'], release_date=phone1['release_date'],lte_exists=phone1['lte_exists'], slug=slugify(phone1['name']))
            
