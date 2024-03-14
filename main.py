from src import categories_worker, pages_worker, format, helpers, json_worker, tests, migrations, db, scraper

import multiprocessing as mp
import sqlite3
import requests, json, os, glob

if __name__ == '__main__':
  product_links = db.get_products_links()
  print(len(product_links))
  