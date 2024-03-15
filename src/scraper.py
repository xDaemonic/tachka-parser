import json, requests, multiprocessing, lxml
from src import pages_worker, helpers, db, format
from bs4 import BeautifulSoup

def catch_links(link: dict):
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
    
  con = db.get_connection()
  cur = con.cursor()
  cur.execute("UPDATE `categories_links` SET proc = 1 WHERE id = ?", (int(link['id']),))
  con.commit()
  
  
def catch_product(link):
  conn = db.get_connection()
  cur = conn.cursor()
  resp = requests.get(link['url'])
  print(link['url'])
  if (resp.status_code == 200):
    data = pages_worker.process_product_page(resp.text, link['url'])
    cur.execute("INSERT INTO products (`url`, `data`) VALUES (?, ?)", (link['url'], json.dumps(data)))
    conn.commit()
    
    cur.execute("UPDATE product_links SET proc = 1 WHERE id = ?", (link['id'],))
    conn.commit()
    
    