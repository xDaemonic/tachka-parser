from src import categories_worker
from src import pages_worker
from src import format
from src import helpers
from src import json_worker
from src import tests
from src import migrations

import multiprocessing as mp
import sqlite3
import requests, json, os

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
  fails = tests.json_files_valid()
  tables = tests.databse_connection()
  print(fails, tables)
  # connection = sqlite3.connect('./sqlite/tachka.db')
  
  # migrations.run(connection)
  # connection.close()
  # fails = tests.json_files_valid()
  # for fail in fails:
  #   path = fail.replace('./json', '').replace('.json', '')
  #   link = {'url': format.url(path), 'proc': False}
  #   os.remove(fail)
  #   scrap_links(link)
    