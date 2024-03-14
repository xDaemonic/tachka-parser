import glob, json, sqlite3
from src import db

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


def databse_connection():
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

def database_table_coluns(table: str) ->list:
  connection = db.get_connection()
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM {table} LIMIT 1")
  
  return [description[0] for description in cursor.description]


def run():
  fails = json_files_valid()
  tables = databse_connection()
  print(tables)
  cols = []
  for table in tables:
    col = database_table_coluns(table)
    col.append(table)
    cols.append(col)
  
  print(fails, tables, cols)