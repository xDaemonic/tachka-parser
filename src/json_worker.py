import json, glob
from src import categories_worker, helpers


def get_product_links():
  files = glob.glob('./json/*.json')
  files = list(map(lambda elem: elem != './json/categories_links.json', files))
  print(files)
  print(len(files))
  