import glob, json, sqlite3
from src import db, categories_worker

def json_files_valid():
  files = glob.glob('./json/*.json')
  fails = []
  
  for file in files:
    try:
      with open(file, 'r+') as fp:
        content = json.load(fp)
        del content
    except Exception:
      fails.append(file)
    finally:
      fp.close()
      
  return fails

def count_categories_files():
  files = glob.glob('./json/*.json')
  files = list(filter(lambda item: item != './json/categories_links.json' , files))
  return len(files)

def database_connection():
  connection = db.get_connection()
  cursor = connection.cursor()
  cursor.execute('''
                  SELECT 
                      name
                  FROM 
                      sqlite_schema
                  WHERE 
                      type ='table' AND 
                      name NOT LIKE 'sqlite_%';
                 ''')
  
  result = cursor.fetchall()
  return [table[0] for table in result]

def database_table_columns(table: str) ->list:
  connection = db.get_connection()
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM {table} LIMIT 1")
  
  return [description[0] for description in cursor.description]

def check_processed_produts():
  conn = db.get_connection()
  cur = conn.cursor()
  
  cur.execute('SELECT * FROM products WHERE EXISTS (SELECT url FROM product_links WHERE product_links.url = products.url AND proc = 1)')
  res = cur.fetchall()
  return len(res)

def run():
  fails = json_files_valid()
  tables = database_connection()
  cnt = count_categories_files()
  cols = []
  for table in tables:
    col = database_table_columns(table)
    col.append(table)
    cols.append(col)
  
  print(fails, cnt, tables, cols)