from src import categories_worker
from src import pages_worker
from src import format
from src import helpers
from src import json_worker

import multiprocessing as mp

import requests, json

def scrap_links(link: dict):
  print('prorcess runned')
  category = format.remove_base_url(link['url']).replace('/', '__')
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
          
  with open(f"./json/{category}.json", 'a+') as f:
    json.dump(result, f)
    f.close()

if __name__ == '__main__':
  # with open(categories_worker.get_category_filepath(), 'a+') as file:
  #   file.truncate(0)
  #   file.close()
  
  categories_links = categories_worker.get_categories_links()
  print(len(categories_links))
  exit(200)
  # categories_links = list(filter(lambda item: not item['proce'], categories_links))
  
  # print(categories_links[0])
  # p = mp.Process(target=scrap_links, args=(link,))
    # p.start()
    # scrap_links(link)
    