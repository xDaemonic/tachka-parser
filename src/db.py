import sqlite3

connection = sqlite3.connect('./sqlite/tachka.db')

def get_connection():
  global connection
  return connection

def get_categories_links() -> list:
  con = get_connection()
  cur = con.cursor()
  
  cur.execute('SELECT * FROM categories_links')
  result = cur.fetchall()
  result = toDict(cur, result)
  for i in range(0, len(result)):
    result[i]['proc'] = bool(result[i]['proc'])
  
  return result

def toDict(cur, data: list):
  if (len(data)):
    for i in range(0, len(data)):
      data[i] =  dict(zip([c[0] for c in cur.description], data[i]))
      
  return data