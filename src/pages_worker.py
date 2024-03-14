import lxml
from bs4 import BeautifulSoup
from src import format

def process_category_page(html: str) -> list:
  soup = BeautifulSoup(html, 'lxml')
  items = soup.find('div', {'class': 'catalog-list'}).find_all('div', {'class': 'catalog-item'})
  return list(map(lambda item: {'url': format.url(item.find('h3', {'class': 'catalog-item__head'}).find('a')['href']), 'proc': False} , items))

def process_product_page(html: str):
  soup = BeautifulSoup(html, 'lxml')
  bc = soup.find('div', {'class': 'dh'}).find_all('span', {'itemprop': 'itemListElement'})
  bc_data = {}
  for i in range(0, len(bc)):
    node = bc[i].find('span', {'itemprop': 'name'})
    if node is None: continue
    
    print(i)
    key = ''
    if i == 1:
      key = 'category'
    elif i == 2:
      key = 'mark'
    elif i == 3:
      key = 'model'
    elif i == 4:
      key = 'years'
    elif i == 5:
      key = 'brand'
    
    bc_data[key] = node.text
  
  res = {
    'fullname': soup.find('h1', {'class': 'product__head'}).text,
    'category': bc_data['category'],
    'bc_data': bc_data,
  }
  
  print(res)
  exit(200)