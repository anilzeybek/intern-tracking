import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = """
                    CREATE TABLE IF NOT EXISTS companies 
                    (id INTEGER serial PRIMARY KEY,
                    name TEXT NOT NULL,
                    country TEXT NOT NULL )
                    """

cursor.execute(create_table)

connection.commit()
connection.close()
