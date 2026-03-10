import sqlite3

file = "test.db"

try:
    with sqlite3.connect(file) as conn:
        print(f"database {file} formed")

except:
    print(f"database {file} not formed")
