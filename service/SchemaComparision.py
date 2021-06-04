# coding: utf-8

from service.TableComparision import TableComparison


class SchemaComparison(object):
    # @ParamType source db.MysqlDatabaseConnector
    # @ParamType target db.MysqlDatabaseConnector
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.source_tables = self.source.database.tables
        self.target_tables = self.target.database.tables
        self.source_tables_dict = self.__tables_to_dict(self.source_tables)
        self.target_tables_dict = self.__tables_to_dict(self.target_tables)

    def compare(self):
        print('start comparing...')

        # self.__new_tables()
        # self.__new_tables_statement()
        exist_tables = self.__exist_tables()
        self.__tables_compare(exist_tables)

    def __tables_to_dict(self, tables):
        a_dict = {}
        for table in tables:
            a_dict.setdefault(table.name, table)
        return a_dict

    # @ReturnType entity.Table list
    def __new_tables(self):
        new_tables = list()
        src = set(self.source_tables_dict.keys())
        dst = set(self.target_tables_dict.keys())
        new_tables_name_list = list(src - dst)
        for table in new_tables_name_list:
            new_tables.append(self.source_tables_dict[table])
        print(new_tables)
        return new_tables

    # Write sql file
    def __new_tables_statement(self):
        # @ReturnType entity.Table list
        new_tables = self.__new_tables()
        for table in new_tables:
            with open('./update/{}.sql'.format(table.name), 'w') as f:
                create_statement = self.source.query_create_table_statement(table.name)
                f.write(create_statement)

    # @ ReturnType entity.Table list
    def __exist_tables(self):
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

    # @ ParamType table entity.Table
    # @ ReturnType entity.TableDiff
    # TODO 新字段 add，变更字段 modify
    def __tables_compare(self, tables):
        tables_diff = list
        for table in tables:
            TableComparison(self.source_tables_dict[table.name], self.target_tables_dict[table.name])


if __name__ == '__main__':
    pass
