# coding: utf-8


class Field(object):
    def __init__(self,table, *args):
        self.__table = table
        self.__field, \
        self.__type, \
        self.__collation, \
        self.__null,\
        self.__key, \
        self.__default, \
        self.__extra, \
        self.__privileges, \
        self.__comment \
            = args

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, a_table):
        self.__table = a_table

    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, a_field):
        self.__field = a_field

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, a_type):
        self.__type = a_type

    @property
    def collation(self):
        return self.__collation

    @collation.setter
    def collation(self, a_collation):
        self.__collation = a_collation

    @property
    def null(self):
        return self.__null

    @null.setter
    def null(self, a_null):
        self.__null = a_null

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, a_key):
        self.__key = a_key

    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, a_default):
        self.__default = a_default

    @property
    def extra(self):
        return self.__extra

    @extra.setter
    def extra(self, an_extra):
        self.__extra = an_extra

    @property
    def privileges(self):
        return self.__privileges

    @privileges.setter
    def privileges(self, some_privileges):
        self.__privileges = some_privileges

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, a_comment):
        self.__comment = a_comment


if __name__ == '__main__':
    pass
