import sqlite3
conn = sqlite3.connect("library.db")
cursor = conn.cursor()
# create a table
cursor.execute("""CREATE TABLE books
                  (title TEXT, author TEXT, release_date TEXT,
                   publisher TEXT, book_type TEXT)
               """)