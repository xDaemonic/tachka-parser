import json, glob
from src import categories_worker, helpers


def get_product_links():
  files = list(filter(lambda elem: elem != './json/categories_links.json', glob.glob('./json/*.json')))
  result = []
  for file in files:
    with open(file, 'r+') as fp:
      content = json.load(fp)
      result = helpers.merge(result, content)
      fp.close()
  
  return result
  