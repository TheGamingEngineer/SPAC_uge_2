import sqlite3 as sql


## make northwind database to load sql file into
data=sql.connect('northwind_database.db')
cursor=data.cursor()

## læs .sql filen
with open('northwind.sql') as file:
    sql_data=file.read()

#cursor.executescript(sql_data)
