import lxml
from bs4 import BeautifulSoup
from src import format

def process_category_page(html: str) -> list:
  soup = BeautifulSoup(html, 'lxml')
  items = soup.find('div', {'class': 'catalog-list'}).find_all('div', {'class': 'catalog-item'})
  return list(map(lambda item: {'url': format.url(item.find('h3', {'class': 'catalog-item__head'}).find('a')['href']), 'proc': False} , items))