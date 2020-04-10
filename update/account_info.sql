alter TABLE account_info add phone_number varchar(50) COLLATE utf8_unicode_ci NULL UNIQUE DEFAULT NULL  ;
alter TABLE account_info add state tinyint(1) NOT NULL DEFAULT 1  ;
alter TABLE account_info add id int(32) NOT NULL PRIMARY KEY DEFAULT NULL auto_increment COMMENT '自增的唯一标识符';
alter TABLE account_info add email varchar(100) COLLATE utf8_unicode_ci NULL UNIQUE  COMMENT '客户登录时所使用的用户名，邮箱';
alter TABLE account_info add customer_id int(20) NULL DEFAULT NULL  ;
