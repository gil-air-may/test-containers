import pymysql.cursors


def get_connection():
    return pymysql.connect(
        host="0.0.0.0",
        user="gervasgu",
        password="gervasgu",
        database="FoodOps",
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor,
    )


def execute_query(query, params=None):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, params or ())
            return cursor.fetchall()


def get_all_tabs():
    sql = "select * from Tab"
    return execute_query(sql)
