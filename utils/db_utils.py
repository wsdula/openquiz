import sqlite3

name = "test.db"


def create_db(path: str, filename: str) -> None:
    fullpath = path + filename
    try:
        with sqlite3.connect(fullpath) as conn:
            print(f"database {fullpath} formed")

    except:
        print(f"database {fullpath} not formed")


create_db("./",name)
