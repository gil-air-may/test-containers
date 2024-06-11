from sqlalchemy import text


def execute_raw_query(engine, raw_query, params=None):
    with engine.connect() as connection:
        result = connection.execute(text(raw_query))
        return result.mappings().all()


def execute_non_query(engine, raw_query, params=None):
    with engine.connect() as connection:
        result = connection.execute(text(raw_query))
        connection.commit()
        return result
