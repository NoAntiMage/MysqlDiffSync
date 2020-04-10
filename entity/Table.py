# coding: utf-8


class Table(object):
    def __init__(self, name, db):
        self.__name = name
        self.__db = db
        self.__fields = list()

    @property
    def name(self):
        return self.__name

    @property
    def db(self):
        return self.__db

    @property
    def fields(self):
        return self.__fields


if __name__ == '__main__':
    table = Table('account','gaussian')
    table.fields.append(1)
    print(table.fields)
