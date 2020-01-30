import sqlite3
from datetime import datetime


class Company:
    def __init__(self, name, country="USA"):
        self.name = name.title()
        self.country = country.upper()

    def save(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        _id = self.__find_id()
        if _id:
            print(f'Company with name {self.name} and country {self.country} already added.')
        else:
            query = 'INSERT INTO companies VALUES(NULL, ?,?,?)'
            cursor.execute(query, (self.name, self.country, datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

            connection.commit()
            connection.close()
            print('DONE')

    def remove(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'DELETE FROM companies WHERE id=?'

        _id = self.__find_id()
        if _id:
            cursor.execute(query, (self.__find_id(),))
            connection.commit()
            connection.close()
            print('DONE')

        else:
            print(f'Company with name {self.name} and country {self.country} not found.')

    def update(self, new_name, new_country):
        new_name = new_name.title() if len(new_name) > 0 else self.name
        new_country = new_country.upper() if len(new_country) > 0 else self.name

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'UPDATE companies SET name=?, country=? WHERE id=?'
        cursor.execute(query, (new_name, new_country, self.__find_id()))

        connection.commit()
        connection.close()

    def check_without_print(self):
        _id = self.__find_id()
        if _id:
            return True
        else:
            return False

    def check(self):
        _id = self.__find_id()
        if _id:
            print(f'Yes! Company with name {self.name} and country {self.country} exists.')
        else:
            print(f'No! Company with name {self.name} and country {self.country} doesnt exists.')

    def __find_id(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT id FROM companies WHERE name=? AND country=?'
        result = cursor.execute(query, (self.name, self.country))
        row = result.fetchone()

        connection.close()

        if row is None:
            return None
        else:
            return row[0]

    @classmethod
    def list_all(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM companies'
        result = cursor.execute(query).fetchall()

        for row in result:
            for attr in row:
                print(attr, end=' ')
            print()
