import json, glob
from src import categories_worker, helpers


def get_product_links():
  files = list(filter(lambda elem: elem != './json/categories_links.json', glob.glob('./json/*.json')))
  print(files)
  print(len(files))
  