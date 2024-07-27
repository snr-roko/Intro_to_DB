import mysql.connector

try:
  book_store_db = mysql.connector.connect(
  host= 'localhost',
  user= 'root',
  passwd = '##############',
  database = 'alx_book_store'
)
except Exception:
  print("Database could not connect, Please check your logins")
else:
  print(f"Database {book_store_db.database} created successfully!")
finally:
  book_store_db.close()
