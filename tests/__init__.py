from testcontainers.mysql import MySqlContainer
import sqlalchemy
from config import connections
from scripts.database import seed_utils
from utils import execute_non_query

mysql = MySqlContainer("mysql:5.7.17", port=3306)
mysql.start()
connections["MYSQL"] = mysql.get_connection_url()

engine = sqlalchemy.create_engine(mysql.get_connection_url())
seed_commands = seed_utils.get_seed_commands()


for statement in seed_commands.split(";"):
    execute_non_query(engine, statement)
