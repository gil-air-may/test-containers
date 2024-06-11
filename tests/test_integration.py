from starlette.testclient import TestClient
import sqlalchemy
from scripts.database import seed_utils
import ipdb
from utils import execute_non_query, execute_raw_query
from config import connections

from testcontainers.mysql import MySqlContainer


mysql = MySqlContainer("mysql:5.7.17", port=3306)
mysql.start()
engine = sqlalchemy.create_engine(mysql.get_connection_url())
connections["MYSQL"] = mysql.get_connection_url()

from main import app

client = TestClient(app)

# ipdb.set_trace()
seed_commands = seed_utils.get_seed_commands()


for statement in seed_commands.split(";"):
    execute_non_query(engine, statement)


def get_all_tabs():
    sql = "select * from Tab"
    return execute_raw_query(engine, sql)


def test_simple_query():
    assert len(get_all_tabs()) == 1


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "world"}


def test_get_all_tabs():
    response = client.get("/tabs")
    assert response.status_code == 200
    assert response.json() == [
        {
            "tab_id": 1,
            "table_number": 1,
            "is_paid": 0,
            "items": '[{"name": "chicken_salad", "amount": 1}]',
            "from_day": "2024-05-18",
            "created_at": "2024-05-18T20:36:42",
        }
    ]
