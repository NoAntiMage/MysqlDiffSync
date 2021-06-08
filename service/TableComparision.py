# coding: utf-8

from service.FieldComparision import FieldComparision


class TableComparison(object):
    """
    :param src: entity.Table
    :param dst entity.Table
    :type src_fields: []entity.Field
    :type dst_fields: []entity.Field
    """
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.src_fields = self.src.fields
        self.dst_fields = self.dst.fields
        self.src_fields_dict = self.__fields_to_dict(self.src_fields)
        self.dst_fields_dict = self.__fields_to_dict(self.dst_fields)
        self.diff = None

    def compare(self):
        # new_fields = self.__new_fields()
        # for field in new_fields:
        #     self.__new_field_statement(field)

        exist_fields = self.__exist_fields()
        self.__fields_compare(exist_fields)

    def __fields_to_dict(self, fields):
        """
        :param fields: []entity.Field
        :rtype: dict[field_name] = Entity.Field
        """
        a_dict = dict()
        for field in fields:
            a_dict.setdefault(field.name, field)
        return a_dict

    def __new_fields(self):
        """
        :rtype new_fields: []entity.Field
        """
        new_fields = list()
        src_fields_list = self.src_fields_dict.keys()
        dst_fields_list = self.dst_fields_dict.keys()
        new_fields_list = list(set(src_fields_list) - set(dst_fields_list))
        for field in new_fields_list:
            new_fields.append(self.src_fields_dict[field])
        return new_fields

    def __new_field_statement(self, field):
        """
        :param field: entity.Field
        :return:
        """
        print('key:  ', field.key)
        sql = ''
        try:
            sql = 'ALTER TABLE `{0.table}` ADD {0.name} {0.type} '.format(field)
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
                with open('./update/add_fields.sql', 'a') as f:
                    f.write(sql)
                    f.write('\n')
            print(sql)

    def __exist_fields(self):
        """
        :return exist_fields: []entity.Field
        """
        exist_fields = list()
        src = self.src_fields_dict.keys()
        dst = self.dst_fields_dict.keys()
        exist_fields_list = list(set(src) & set(dst))
        for field in exist_fields_list:
            exist_fields.append(self.src_fields_dict[field])
        return exist_fields

    def __fields_compare(self, fields):
        """
        :param fields: []entity.Field
        :return:
        """
        # print("compare table `{0}`".format(self.src.name))
        for field in fields:
            fc = FieldComparision(self.src_fields_dict[field.name], self.dst_fields_dict[field.name])
            fc.compare()
