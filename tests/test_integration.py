from starlette.testclient import TestClient
from main import app
import ipdb

import pymysql.cursors


from testcontainers.mysql import MySqlContainer

client = TestClient(app)
mysql = MySqlContainer("mysql:5.7.17")


def get_connection():
    return pymysql.connect(mysql.get_connection_url())


def execute_query(query, params=None):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, params or ())
            return cursor.fetchall()


def get_all_tabs():
    sql = "select * from Tab"
    return execute_query(sql)


def test_simple_query():
    print(get_all_tabs())


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "dude"}
