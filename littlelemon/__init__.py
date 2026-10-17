import pymysql
from django.db.backends.base.base import BaseDatabaseWrapper

# 1. Alias pymysql as MySQLdb
pymysql.install_as_MySQLdb()

# 2. Bypass Django 5.2+ strict MySQL 8.4 version check for MySQL 8.0.x
BaseDatabaseWrapper.check_database_version_supported = lambda self: None