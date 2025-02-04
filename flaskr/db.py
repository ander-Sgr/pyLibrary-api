import sqlite3
DB_NAME = "pycommerce.db"

def init_db(DB_NAME):
    with sqlite3.connect(DB_NAME) as conn:
        with open("scheme.sql", "r") as file:
            conn.executescript(file.read())
    print(f"DB {DB_NAME} initialized")


if __name__ == "__main__":
    init_db(DB_NAME)