from src import categories_worker
from src import pages_worker
from src import format
from src import helpers
from src import json_worker
from src import tests
from src import migrations
from src import db
from src import scraper

import multiprocessing as mp
import sqlite3
import requests, json, os, glob

if __name__ == '__main__':
  links = db.get_unprocessed_categories_links()
  for link in links:
    scraper.catch_links(link)
  # con = db.get_connection()
  # cur = con.cursor()
  
  # cur.execute(f"UPDATE `categories_links` SET proc = 0 WHERE url = ?", ('https://tachka.ru/tormoza/tormozniye-shlangi',))
  # con.commit()
  