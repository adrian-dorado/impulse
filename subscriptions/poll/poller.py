from urllib import response
import django
import os
import sys
import time
import json
import requests


sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "subscriptions.settings")
django.setup()

from subscriptions_rest.models import ProductInventoryVO, ClothingInventoryVO

products_url = f"{os.environ['PRODUCTS']}/products"
clothing_url = f"{os.environ['PRODUCTS']}/clothing"


def get_product_inventory():
    response = requests.get(products_url)
    content = json.loads(response.content)
    for product in content["products"]:
        ProductInventoryVO.objects.update_or_create(id=product["id"])


def get_clothing_inventory():
    response = requests.get(clothing_url)
    content = json.loads(response.content)
    for clothing in content["clothes"]:
        ClothingInventoryVO.objects.update_or_create(id=clothing["id"])


def poll():
    while True:
        try:
            print("Subscriptions poller polling for data")
            get_product_inventory()
            get_clothing_inventory()
            print("cheese")
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(10)


if __name__ == "__main__":
    poll()
