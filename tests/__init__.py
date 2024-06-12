from testcontainers.mysql import MySqlContainer
from testcontainers.redis import RedisContainer
import sqlalchemy
from config import connections
from scripts.database import seed_utils
from utils import execute_non_query
import json
import ipdb

mysql = MySqlContainer("mysql:5.7.17", port=3306)
mysql.start()
connections["MYSQL"] = mysql.get_connection_url()

engine = sqlalchemy.create_engine(mysql.get_connection_url())
seed_commands = seed_utils.get_seed_commands()

for statement in seed_commands.split(";"):
    execute_non_query(engine, statement)

redis_container = RedisContainer().__enter__()
redis_client = redis_container.get_client()
redis_conn = redis_client.get_connection_kwargs()

# ipdb.set_trace()

redis_client.set(
    1,
    json.dumps(
        {
            "tab_id": 1,
            "table_number": 1,
            "is_paid": 0,
            "items": '[{"name": "chicken_salad", "amount": 1}]',
            "from_day": "2024-05-18",
            "created_at": "2024-05-18T20:36:42",
        },
    ),
)

connections["REDIS"]["host"] = redis_conn["host"]
connections["REDIS"]["port"] = redis_conn["port"]
