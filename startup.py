import sqlite3


def startup():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    create_table = """
                        CREATE TABLE IF NOT EXISTS companies (
                            id INTEGER PRIMARY KEY autoincrement,
                            name TEXT NOT NULL,
                            country TEXT NOT NULL,
                            dt datetime NOT NULL
                        )
                        """

    cursor.execute(create_table)

    connection.commit()
    connection.close()
