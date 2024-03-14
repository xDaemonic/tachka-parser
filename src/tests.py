import glob, json, sqlite3

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
  connection = sqlite3.connect('./sqlite/tachka.db')
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

  return cursor.fetchall()