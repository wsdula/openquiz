from pathlib import Path
import sqlite3
from typing import Dict

DB_PATH = Path("test.db")


class TriviaDB:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._initialize_db()

    SCHEMA_FUNCTIONS = [
        "_create_collections_questions_table",
        "_create_questions_table",
        "_create_collections_table",
    ]

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _initialize_db(self):
        with self._connect() as conn:
            for func_name in self.SCHEMA_FUNCTIONS:
                getattr(self, func_name)(conn)

    def _create_questions_table(self, conn: sqlite3.Connection) -> None:
        try:
            query = """
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt TEXT,
                answer TEXT,
                category TEXT,
                value INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """

            conn.execute(query)
            print("Table 'questions' successfully created or already exists")

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def _create_collections_table(self, conn: sqlite3.Connection) -> None:
        try:
            query = """
            CREATE TABLE IF NOT EXISTS collections (
            id INTEGER PRIMARY KEY,
            description TEXT
            )
            """

            conn.execute(query)
            print("Table 'collections' successfully created or already exists")

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def _create_collections_questions_table(self, conn: sqlite3.Connection) -> None:
        try:
            query = """
            CREATE TABLE IF NOT EXISTS collquestions (
            collection_id INTEGER,
            question_id INTEGER,
            PRIMARY KEY (collection_id, question_id),
            FOREIGN KEY(collection_id) REFERENCES collections(id),
            FOREIGN KEY(question_id) REFERENCES questions(id)
            )
            """

            conn.execute(query)
            print("Table 'collquestions' successfully created or already exists")

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def add_question(self, question_data: Dict):
        with self._connect() as conn:
            query = """
            INTER INTO questions
            (prompt, answer, category, value)
            VALUES (?, ?, ?, ?)
            """

            cur = conn.execute(
                query,
                (
                    question_data["prompt"],
                    question_data["answer"],
                    question_data["category"],
                    question_data["value"],
                ),
            )
            return cur.lastrowid


db = TriviaDB()
