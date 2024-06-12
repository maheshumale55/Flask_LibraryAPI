import sqlite3

conn = sqlite3.connect('books.sqlite')

cursor = conn.cursor()
sql_query = """ CREATE TABLE book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL  
)"""
sql_select_all = "select * from book"

#sql_insert = "INSERT INTO book VALUES (1, 'Mahesh Umale', 'English', 'C')"

# cursor.execute(sql_insert)
cursor.execute(sql_select_all)

print(cursor.fetchall())
