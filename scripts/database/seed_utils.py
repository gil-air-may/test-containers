def get_seed_commands():
    with open("scripts/database/seeds.sql", "r") as file:
        content = file.read()
        return content
