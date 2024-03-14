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
  conn = db.get_connection()
  cur = conn.cursor()
  
  cur.execute('SELECT COUNT(*) FROM product_links')
  print(cur.fetchone())
  # links = json_worker.get_product_links()
  # conn = db.get_connection()
  # cur = conn.cursor()
  
  # for link in links:
  #   cur.execute("INSERT INTO `product_links` (`url`, `proc`) VALUES (?, ?) ON CONFLICT(url) DO UPDATE SET url = url", (link['url'], bool(link['proc'])))
  #   conn.commit()
    
  # conn.close()