from starlette.testclient import TestClient
from main import app
import sqlalchemy
from sqlalchemy import text
import ipdb
from scripts import utils


from testcontainers.mysql import MySqlContainer


client = TestClient(app)
mysql = MySqlContainer("mysql:5.7.17")
mysql.start()

engine = sqlalchemy.create_engine(mysql.get_connection_url())
seed_commands = utils.get_seed_commands()


def execute_raw_query(raw_query, params=None):
    with engine.connect() as connection:
        result = connection.execute(text(raw_query))
        return result.mappings().all()


def execute_non_query(raw_query, params=None):
    with engine.connect() as connection:
        result = connection.execute(text(raw_query))
        connection.commit()
        return result


for statement in seed_commands.split(";"):
    execute_non_query(statement)

print(mysql.get_connection_url())
insert = seed_commands.split(";")[2]


def get_all_tabs():
    sql = "select * from Tab"
    return execute_raw_query(sql)


def test_simple_query():
    print(get_all_tabs())


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "world"}
