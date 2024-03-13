from src import categories_worker
from src import pages_worker
from src import format
from src import helpers

import requests, json

if __name__ == '__main__':
  categories_links = categories_worker.get_categories_links()
  for link in categories_links:
    category = format.remove_base_url(link['url'])
    resp = requests.get(link['url'])
    page = 0
    result = []
    while resp.status_code == 200:
      print(f"category: {category}, page: {page}\r\n")
      links = pages_worker.process_category_page(resp.text)
      result = helpers.merge(result, links)
      
      page += 1
      path = format.page_url(link['url'], page)
      resp = requests.get(path)
      
    with open(f"./json/{category}.json", 'a+') as file:
      json.dump(result, file)
      file.close()
    