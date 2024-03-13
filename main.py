from src import categories_worker
from src import pages_worker
from src import format
from src import helpers
from src import json_worker

import multiprocessing as mp

import requests, json

def scrap_links(link: dict):
  category = format.remove_base_url(link['url'])
  resp = requests.get(link['url'], proxies=proxies)
  print(resp.status_code)
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

  json_worker.set_process_category_status(link['url'], True)

if __name__ == '__main__':
  categories_links = categories_worker.load_categories_links()
  proxies = {
    'https': 'https://185.225.232.191:80'
  }
  
  process_list = []
  for link in categories_links:
    p = mp.Process(scrap_links,[link])
    print(p)
  
  map(lambda process: process.start(), process_list)
  map(lambda process: process.join(), process_list)
    