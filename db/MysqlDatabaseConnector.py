# coding: utf-8

import pymysql
import json
from db.DatabaseConnector import DatabaseConnector
from entity.Database import Database
from entity.Table import Table
from entity.Field import Field

TIME_OUT = 10


class MysqlDatabaseConnector(DatabaseConnector):
    """
    :param config: obj deserialized from json file

    MysqlDatabaseConnector
    |
    Database
    |
    Tables
    |
    Fields
    """
    def __init__(self, config):
        super(MysqlDatabaseConnector, self).__init__()
        try:
            self.database = Database(config['database'])
            self.__db = pymysql.connect(**config, connect_timeout=TIME_OUT)
            self.__cursor = self.__db.cursor()
        except Exception as e:
            print(e)

    @property
    def db(self):
        return self.__db

    @property
    def cursor(self):
        return self.__cursor

    def get_version(self):
        self.__cursor.execute("""SELECT VERSION();""")
        version = self.__cursor.fetchone()
        return version

    def fetch_tables(self):
        self.__cursor.execute("""SHOW TABLES;""")
        result = self.__cursor.fetchall()
        # print(result)
        for l in result:
            a_table = Table(l[0], self.database)
            self.database.tables.append(a_table)

    def query_fields(self, a_table):
        """
        :param a_table:
        :return [][]
        """
        self.__cursor.execute("""SHOW FULL COLUMNS FROM `{}`;""".format(a_table))
        return self.cursor.fetchall()

    def fetch_fields_of_all_tables(self):
        tables = self.database.tables
        for table in tables:
            fields = self.query_fields(table.name)
            for f in fields:
                field = Field(table.name, *f)
                table.fields.append(field)

    def fetch(self):
        self.fetch_tables()
        self.fetch_fields_of_all_tables()

    def query_create_table_statement(self, table):
        self.__cursor.execute("""SHOW CREATE TABLE {};""".format(table))
        result = self.__cursor.fetchall()
        print(result[0][1])
        return '{};'.format(result[0][1])


if __name__ == '__main__':
    with open('/Users/wujimaster/data/MysqlDiffSync/db.json', 'rb') as f:
        db_config = json.load(f)
    # print(db_config)
    mysql = MysqlDatabaseConnector(db_config['source'])
    mysql.fetch()
    tables = mysql.database.tables
    for table in tables:
        print("---")
        print(table.name)
        for f in table.fields:
            print(f.__dict__)
    print("\n\n\n")


