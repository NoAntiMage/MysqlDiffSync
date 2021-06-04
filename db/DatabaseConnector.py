# coding: utf-8


class DatabaseConnector(object):

    def __init__(self):
        pass

    # @ReturnType entity.Table list
    def query_tables(self):
        pass

    # @ParamType table string
    # @ReturnType entity.Field list
    def query_fields(self, table):
        pass

    # @ParamType diff entity.Diff
    # @ReturnType boolean
    def sync(self, diff):
        pass
