from ..infrastructure.db import tab_db


def get_all_tabs():
    return tab_db.get_all_tabs()


def get_todays_tabs():
    return tab_db.get_todays_tabs()
