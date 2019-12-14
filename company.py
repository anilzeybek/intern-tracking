import sqlite3


class Company:
    def __init__(self, name, country="USA"):
        self.name = name
        self.country = country

    def save(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'INSERT INTO companies VALUES(NULL, ?,?)'
        cursor.execute(query, (self.name, self.country))

        connection.commit()
        connection.close()

    def remove(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'DELETE FROM companies WHERE id=?'
        cursor.execute(query, (self.__find_id(),))

        connection.commit()
        connection.close()

    def __find_id(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT id FROM companies WHERE name=? AND country=?'
        result = cursor.execute(query, (self.name, self.country))
        row = result.fetchone()
        print(row)

        connection.commit()
        connection.close()

        # return something here
