import json, requests
from src import pages_worker, helpers

def catch_links(link: dict):
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