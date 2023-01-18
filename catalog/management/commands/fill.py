from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Products = [
            {'name_product': 'apple', 'title': 'useful', 'image': '', 'category_id': '1', 'price': '3',
             'date_create': '2021-12-31 15:25:00+01',
             'date_update': '2021-12-31 15:25:00+01'},
            {'name_product': 'bananas', 'title': 'useful', 'image': '', 'category_id': '1', 'price': '5',
             'date_create': '2021-12-31 15:25:00+01',
             'date_update': '2021-12-31 15:25:00+01'},
        ]
        Categories = [
            {'category_name': 'vegetables', 'title': 'useful but not tasty'},
            {'category_name': 'milk', 'title': 'white, fat'},
        ]

        products_list = []
        categories_list = []

        for item in Products:
            products_list.append(Product(**item))

        for item in Categories:
            categories_list.append(Category(**item))

        Product.objects.all().delete()
        Product.objects.bulk_create(products_list)

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_list)
