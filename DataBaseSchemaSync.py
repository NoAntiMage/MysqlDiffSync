# coding: utf-8

from pymysql import OperationalError
import sys
import os
import json
import shutil
from dao.MysqlDatabaseConnector import MysqlDatabaseConnector
from service.SchemaComparision import SchemaComparison
from util.Configer import Configer


class DataBaseSchemaSync(object):
    def __init__(self, conf_path = None):
        try:
            configure = Configer(conf_path)
        except IOError:
            sys.stderr.write('configure file not exist.')
            sys.exit(1)

        self.db_config = json.loads(configure.config)

        try:
            self.source = MysqlDatabaseConnector(self.db_config['source'])
            self.source.fetch()
        except OperationalError:
            sys.stderr.write('database source connect error.')
            sys.exit(1)

        try:
            self.target = MysqlDatabaseConnector(self.db_config['target'])
            self.target.fetch()
        except OperationalError:
            sys.stderr.write('database target connect error.')
            sys.exit(1)

    def compare(self):
        if os.path.exists('update'):
            shutil.rmtree('update')
            os.mkdir('update')
        sc = SchemaComparison(self.source, self.target)
        sc.compare()


if __name__ == '__main__':
    foo = DataBaseSchemaSync()
    # for table in foo.source.database.tables:
    #     print(table.name)
    if len(sys.argv) <= 1:
        foo = DataBaseSchemaSync()
    else:
        foo = DataBaseSchemaSync(sys.argv[1])

    foo.compare()
