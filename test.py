from src import tests, db

conn = db.get_connection()
cur = conn.cursor()
cur.execute('SELECT COUNT(*) FROM product_links WHERE proc = 0')
print("unproc links count")
print(cur.fetchone())

cur.execute('SELECT COUNT(*) FROM products')
print('products count')
print(cur.fetchone())

cur.execute('SELECT COUNT(*) FROM product_links')
print('total poroduct links')
print(cur.fetchone())