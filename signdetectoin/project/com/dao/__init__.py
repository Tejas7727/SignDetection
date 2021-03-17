import pymysql
def condb():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='pythondb',
                           cursorclass=pymysql.cursors.DictCursor
                           )

