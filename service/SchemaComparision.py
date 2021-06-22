# coding: utf-8

from service.TableComparision import TableComparison


class SchemaComparison(object):
    """
    :param source: entity.MysqlDatabaseConnector
    :param target: entity.MysqlDatabaseConnector
    :type source_tables: []Tables
    :type target_tables: []Tables
    """
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.source_tables = self.source.database.tables
        self.target_tables = self.target.database.tables
        self.source_tables_dict = self.__tables_to_dict(self.source_tables)
        self.target_tables_dict = self.__tables_to_dict(self.target_tables)

    def compare(self):
        print('start comparing...')

        self.__new_tables()
        self.__new_tables_statement()

        exist_tables = self.__exist_tables()
        self.__tables_compare(exist_tables)

    def __tables_to_dict(self, tables):
        """
        :param tables: []entity.Table
        :rtype dict[Table.name] = Table.obj
        """
        a_dict = {}
        for table in tables:
            a_dict.setdefault(table.name, table)
        return a_dict

    def __new_tables(self):
        """
        :return new_table: []entity.Table
        """
        new_tables = list()
        src = set(self.source_tables_dict.keys())
        dst = set(self.target_tables_dict.keys())
        new_tables_name_list = list(src - dst)
        for table in new_tables_name_list:
            new_tables.append(self.source_tables_dict[table])
        # print(new_tables)
        return new_tables

    def __new_tables_statement(self):
        """
        Write CREATE TABLE SQL to file
        """
        new_tables = self.__new_tables()
        for table in new_tables:
            with open('./update/create_tables.sql', 'a') as f:
                create_statement = self.source.query_create_table_statement(table.name)
                f.write(create_statement)
                f.write('\n')

    def __exist_tables(self):
        """
        :rtype exist_tables: []entity.Table
        """
        exist_tables = list()
        src = set(self.source_tables_dict.keys())
        dst = set(self.target_tables_dict.keys())
        exist_tables_name_list = list(src & dst)
        for table in exist_tables_name_list:
            exist_tables.append(self.source_tables_dict[table])
        # print(exist_tables)
        # for table in exist_tables:
        #     print(table.name)
        return exist_tables

    def __tables_compare(self, tables):
        """
        :param tables: []entity.Table
        :return:
        """
        for table in tables:
            tc = TableComparison(self.source_tables_dict[table.name], self.target_tables_dict[table.name])
            tc.compare()


if __name__ == '__main__':
    pass
