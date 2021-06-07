# coding: utf-8


class FieldComparision(object):
    """
    :param src: dict[field_name] = entity.Field
    :param dst: dict[field_name] = entity.Field
    """
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def compare(self):
        sql = ''
        try:
            if self.src.type != self.dst.type \
                    or self.src.null != self.dst.null \
                    or self.src.default != self.dst.default:
                sql = "ALTER TABLE `{0.table}` MODIFY COLUMN {0.name} ".format(self.src)
                sql += "{} ".format(self.src.type)

                if self.src.null == "YES":
                    sql += "NULL "
                elif self.src.null == "NO":
                    sql += "NOT NULL "
                    if self.src.default is not None:
                        sql += "DEFAULT {} ".format(self.src.default)
        except Exception as e:
            print(e)
        finally:
            if len(sql) != 0:
                sql += ';'
                with open('./update/alter.sql', 'a') as f:
                    f.write(sql)
                    f.write('\n')
            print(sql)
