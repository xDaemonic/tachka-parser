import lxml, re
from bs4 import BeautifulSoup
from src import format

def process_category_page(html: str) -> list:
  soup = BeautifulSoup(html, 'lxml')
  items = soup.find('div', {'class': 'catalog-list'}).find_all('div', {'class': 'catalog-item'})
  return list(map(lambda item: {'url': format.url(item.find('h3', {'class': 'catalog-item__head'}).find('a')['href']), 'proc': False} , items))

def process_product_page(html: str, link):
  soup = BeautifulSoup(html, 'lxml')
  
  fullname_node = soup.find('h1', {'class': 'product__head'})
  fullname = fullname_node.text.strip() if fullname_node is not None else ''
  
  bc_node = soup.find('div', {'class': 'dh'}).find_all('span', {'itemprop': 'itemListElement'})
  bc_data = catch_bc(bc_node) if bc_node is not None else {}
  
  brand_node = soup.find('div', {'itemprop': 'brand'})
  bn_data = catch_tech(brand_node) if brand_node is not None else {}
  
  attrs_node = soup.find('table', {'class': 'attribute_table_off'})
  an_data = catch_tech(attrs_node) if attrs_node is not None else {}
  
  image_node = soup.find('div', {'class': 'product-short__image'})
  image = ''
  if image_node is not None:
    if image_node.find('carousel') is not None:
      image = image_node.find('carousel').find('div', {'class': 'tns-slide-active'}).find('a')['href']
    elif image_node.find('a', {'class': 'glightbox'}):
      image = image_node.find('a', {'class': 'glightbox'})['href']
      
  descr_node = soup.find('meta', {'itemprop': 'description'})
  description = ''
  cross = ''
  modify = ''
  
  if descr_node is not None:
    description = descr_node['content']
    
    if "Кросс коды" in description:
      r2 = re.compile(r"^.*?Кросс коды\s+(.*?)[а-яА-Я]+.*$", re.IGNORECASE | re.DOTALL)
      cross = r2.sub('\g<1>', description)
      cross = re.sub(r"^\s+", '', cross, flags=re.MULTILINE).split("\n")
      cross = list(filter(lambda item: len(item), cross))

    if "Подходит для следующих модификаций:" in description:
      r3 = re.compile(r"^.*?Подходит для следующих модификаций:\s+(.*?)$", re.IGNORECASE | re.DOTALL)
      modify = r3.sub('\g<1>', description)
      modify = re.split(r"^\n+", modify, flags=re.MULTILINE)
      modify = list(map(lambda item: re.sub(r"\n\s+", '| ', item, flags=re.MULTILINE|re.IGNORECASE).strip(), modify))

  return {
    'fullname': fullname,
    'category': bc_data['category'] if 'category' in bc_data.keys() else '',
    'brand': bc_data['brand'] if 'brand' in bc_data.keys() else '',
    'article': an_data[-1]['value'] if len(an_data) else '',
    'description': description,
    'image': image,
    'cross': cross,
    'modify': modify,
    'bc_data': bc_data,
    'bn_data': bn_data,
    'an_data': an_data,
  }
  
  
def catch_tech(soup):
  result = []
  tr_list = soup.find_all('tr')
  for tr in tr_list:
    td_list = tr.find_all('td')
    
    val = td_list[1].text
    if td_list[1].find('img') is not None:
      src = td_list[1].find('img')['src']
      val = f"https://tachka.ru{src}"
    
    result.append({'name': td_list[0].text.strip(), 'value': val.strip()})
    
  return result

def catch_bc(soup):
  bc_data = {}
  for i in range(0, len(soup)):
    node = soup[i].find('span', {'itemprop': 'name'})
    if node is None: continue
    
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
    
  return bc_data