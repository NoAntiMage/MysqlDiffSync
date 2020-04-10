# coding: utf-8


class Database(object):
    def __init__(self, config):
        self.__name = None
        self.__tables = list()
        self.__charset = None
        self.__collate = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, db_name):
        self.__name = db_name

    @property
    def tables(self):
        return self.__tables

    @property
    def charset(self):
        return self.__charset

    @charset.setter
    def charset(self, charset):
        self.__charset = charset

    @property
    def collate(self):
        return self.__collate

    @collate.setter
    def collate(self, collate):
        self.__collate = collate


if __name__ == '__main__':
    db = Database(1)
    print(db.tables)
    db.tables.append('wuji')
    print(db.tables)
