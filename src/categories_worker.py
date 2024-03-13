import requests, lxml, json, os
from bs4 import BeautifulSoup
from src import format

categories_links_url = 'https://tachka.ru/zapchasti'
categories_links_filepath = './json/categories_links.json'

def load_categories_links():
  resp = requests.get(categories_links_url)
  soup = BeautifulSoup(resp.text, 'lxml')
  categories = soup.find('ul', {'class': 'more-items__list'}).find_all('a')
  categories = list(map(lambda item: { 'url': format.url(item['href']), 'proc': False }, categories))

  if not os.path.isdir('./json'):
    os.mkdir('./json', 644)
  
  with open(categories_links_filepath, 'a+') as file:
    json.dump(categories, file)
    file.close()
    
  return categories
    
def get_category_filepath() -> str:
  global categories_links_filepath
  return categories_links_filepath
    
def get_categories_links():
  global categories_links_filepath
  file = open(categories_links_filepath, 'r+')
  result = json.load(file)
  file.close()
  return result

def set_categories_filepath(path: str):
  global categories_links_filepath
  categories_links_filepath = path

def set_categories_links_url(url: str):
  global categories_links_url
  categories_links_url = url