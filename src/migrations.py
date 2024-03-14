commands = [
  'CREATE TABLE IF NOT EXISTS `categories_links` (id INTEGER PRIMARY KEY, url TEXT, proc TINYINT)',
  'CREATE TABLE IF NOT EXISTS `categories_files` (id INTEGER PRIMARY KEY, url TEXT, proc TINYINT)',
]

def get_list() -> list:
  global commands
  return commands

def run(connection) -> None:
  cursor = connection.cursor()
  ml = get_list()
  for cmd in ml:
    cursor.execute(cmd)
    connection.commit()