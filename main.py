from src import categories_worker
from src import pages_worker
from src import format
from src import helpers
from src import json_worker

import multiprocessing as mp

import requests, json

def scrap_links(link: dict):
  print('prorcess runned')
  category = format.remove_base_url(link['url']).replace('/', '-')
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
  categories_links = categories_worker.get_categories_links()
  # for i in range(0, len(categories_links)):
  #   if categories_links[i]['url'] == 'https://tachka.ru/tormoza/tormozniye-shlangi':
  #     break
  #   categories_links[i]['proc'] = True
    
  # with open(categories_worker.get_category_filepath(), 'w+') as file:
  #   file.truncate()
  #   json.dump(categories_links, file)
  #   file.close()
  
  # print('ok')
  # exit(200)     
  categories_links = list(filter(lambda item: not item['proc'], categories_links))
  for link in categories_links:
  # print(categories_links[0])
  # p = mp.Process(target=scrap_links, args=(link,))
    # p.start()
    scrap_links(link)
    