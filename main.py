from src import categories_worker
from src import pages_worker
from src import format
from src import helpers

from multiprocessing import Pool

import requests, json

def scrap_links(link: dict):
  category = format.remove_base_url(link['url'])
  resp = requests.get(link['url'], proxies=proxies)
  page = 0
  result = []
  while resp.status_code == 200:
    print(f"category: {category}, page: {page}\r\n")
    links = pages_worker.process_category_page(resp.text)
    result = helpers.merge(result, links)
    
    page += 1
    path = format.page_url(link['url'], page)
    resp = requests.get(path, proxies=proxies)
          
  with open(f"./json/{category}.json", 'a+') as file:
    json.dump(result, file)
    file.close()


if __name__ == '__main__':
  print('ok')
  categories_links = categories_worker.load_categories_links()
  proxies = {
    'https': 'https://185.225.232.191:80'
  }
  pool = Pool(10)
  for link in categories_links:
    pool.apply_async(scrap_links, link)
  
    