import sqlalchemy
from sqlalchemy import text

engine = sqlalchemy.create_engine("mysql+mysqldb://gervasgu:gervasgu@0.0.0.0/FoodOps")


def execute_raw_query(raw_query, params=None):
    with engine.connect() as connection:
        result = connection.execute(text(raw_query))
        return result.mappings().all()


def get_all_tabs():
    sql = "select * from Tab"
    return execute_raw_query(sql)
