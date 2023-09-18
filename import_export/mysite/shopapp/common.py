from csv import DictReader
from io import TextIOWrapper
from typing import Sequence

from django.contrib.auth.models import User

from shopapp.models import Product, Order


def save_csv_products(file, encoding):
    csv_file = TextIOWrapper(
        file,
        encoding=encoding,
    )
    reader = DictReader(csv_file)

    products = [
        Product(**row)
        for row in reader
    ]
    Product.objects.bulk_create(products)
    return products


def save_csv_orders(file, encoding):
    csv_file = TextIOWrapper(
        file,
        encoding=encoding,
    )
    reader = DictReader(csv_file)
    user = User.objects.get(username="admin")
    products: Sequence[Product] = Product.objects.only("id").all()
    for row in reader:
        order, created = Order.objects.get_or_create(
            delivery_address=row['delivery_address'],
            promocode=row["promocode"],
            user=user
        )
    for product in products:
        order.products.add(product)

    return order
