import pymysql

# 因为python3.*不支持MySQLdb，所以只能用这个代替
pymysql.install_as_MySQLdb()