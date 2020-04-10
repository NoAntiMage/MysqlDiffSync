# coding: utf-8


class TableComparison(object):
    # @ParamType src entity.Table
    # @ParamType dst entity.Table
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.src_fields = self.src.fields
        self.dst_fields = self.dst.fields
        self.src_fields_dict = self.__fields_to_dict(self.src_fields)
        self.dst_fields_dict = self.__fields_to_dict(self.dst_fields)
        self.diff = None
        self.compare()

    def compare(self):
        new_fields = self.__new_fields()
        for field in new_fields:
            self.__new_field_statement(field)


    def __fields_to_dict(self, fields):
        a_dict = dict()
        for field in fields:
            a_dict.setdefault(field.field, field)
        return a_dict

    # @ReturnType entity.Field list
    def __new_fields(self):
        new_fields = list()
        src_fields_list = self.src_fields_dict.keys()
        dst_fields_list = self.dst_fields_dict.keys()
        new_fields_list = list(set(src_fields_list) - set(dst_fields_list))
        for field in new_fields_list:
            new_fields.append(self.src_fields_dict[field])
        return new_fields

    # @ParamType entity.Field
    def __new_field_statement(self, field):
        print('key:  ',field.key)
        sql = ''
        try:
            sql = 'alter TABLE {0.table} add {0.field} {0.type} '.format(field)
            if field.collation is not None:
                sql += 'COLLATE {0.collation} '.format(field)

            if field.null == 'YES':
                sql += 'NULL '
            elif field.null == 'NO':
                sql += 'NOT NULL '

            if field.key is None:
                pass

            if field.key == 'PRI':
                sql += 'PRIMARY KEY '
            elif field.key == 'UNI':
                sql += 'UNIQUE '

            if field.default is None:
                sql += 'DEFAULT NULL '
            elif field.default is not None and isinstance(field.default, str):
                if field.default == '':
                    pass
                else:
                    sql += 'DEFAULT {0.default} '.format(field)

            if field.extra is not None:
                sql += '{0.extra} '.format(field)

            if len(field.comment) > 0:
                sql += "COMMENT '{0.comment}'".format(field)
        except Exception as e:
            print(e)
        finally:
            if len(sql) != 0:
                sql += ';'
                with open('./update/{}.sql'.format(field.table), 'a') as f:
                    f.write(sql)
                    f.write('\n')
            print(sql)


    def __exist_fields(self):
        pass
    # todo 获取相同的同名字段

    def __field_compare(self):
        pass
    # todo 比较相同字段的属性 FieldComparision