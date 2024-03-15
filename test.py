from src import tests, db

conn = db.get_connection()
cur = conn.cursor()
cur.execute('SELECT COUNT(*) FROM product_links WHERE proc = 0')
print(cur.fetchone())