# coding: utf-8

CONFIG_FILE_PATH = '/Users/wujimaster/data/MysqlDiffSync/db.json'


class Configer(object):
    def __init__(self, config_path=None):
        if config_path:
            of = open(config_path)
        else:
            of = open(CONFIG_FILE_PATH)

        self.__config = of.read()

    @property
    def config(self):
        return self.__config


if __name__ == '__main__':
    print(Configer().config)
