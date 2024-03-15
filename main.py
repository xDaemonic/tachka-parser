from src import categories_worker, pages_worker, format, helpers, json_worker, tests, migrations, db, scraper

import multiprocessing as mp
import sqlite3
import requests, json, os, glob

if __name__ == '__main__':
  # scraper.catch_product('https://tachka.ru/akkumulyator/chevrolet/cruze/2/acdelco-19375462-2500')
  migrations.run(db.get_connection())
  print(tests.database_table_columns('products'))
  exit(200)
  product_links = db.get_unprocessed_products_links()
  product_links = helpers.chunks(product_links, 25)
  for chunk in product_links:
    process_list = []
    for elem in chunk:
      # process = mp.Process(target=scraper.catch_product, args=(elem['url'],))
      # process.start()
      # process_list.append(process)
      scraper.catch_product(elem['url'])
      
    # for process in process_list:
    #   process.join()
