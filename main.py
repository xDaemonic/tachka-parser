from src import categories_worker
from src import pages_worker
from src import format
from src import helpers
from src import json_worker
from src import tests
from src import migrations
from src import db

import multiprocessing as mp
import sqlite3
import requests, json, os, glob

if __name__ == '__main__':
  links = db.get_unprocessed_categories_links()
  print(links)