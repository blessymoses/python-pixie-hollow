import sqlite3


class Schema:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("todo.db")
        self.create_user_table()
        self.create_todo_table()

    def create_todo_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS 'todo'(
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                is_done BOOLEAN,
                is_deleted BOOLEAN DEFAULT 0,
                created_on DATE DEFAULT CURRENT_DATE,
                due_date DATE,
                user_id INTEGER FOREIGNKEY REFERENCES user(id)
            );
        """
        self.conn.execute(query)

    def create_user_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS 'user'(
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            );
        """
        self.conn.execute(query)


class ToDoModel:
    table_name = "todo"

    def __init__(self) -> None:
        self.conn = sqlite3.connect("todo.db")

    def __del__(self) -> None:
        self.conn.commit()
        self.conn.close()

    def create(self, title, description):
        query = f"INSERT INTO {self.table_name}(title, description) \
            VALUES('{title}', '{description}')"
        print(query)
        result = self.conn.execute(query)
        print(result.lastrowid)
        return result.lastrowid

    def select(self, where_clause=""):
        columns = ["id", "title", "description", "due_date", "is_done", "is_deleted"]
        query = (
            f"SELECT {', '.join(columns)} \
            FROM {self.table_name} WHERE is_deleted != {1} "
            + where_clause
        )
        print(query)
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [
            {column: row[i] for i, column in enumerate(columns)} for row in result_set
        ]
        return result

    def select_by_id(self, _id):
        where_clause = f"AND id = {_id}"
        return self.select(where_clause)

    def delete(self, item_id):
        query = f"UPDATE {self.table_name} SET is_deleted = {1} \
            WHERE id = {item_id}"
        self.conn.execute(query)
        return self.select()

    def update(self, item_id, update_dict):
        set_clause = ", ".join(
            [f"{column} = '{value}'" for column, value in update_dict.items()]
        )
        query = f"UPDATE {self.table_name} SET {set_clause} \
            WHERE id = {item_id}"
        self.conn.execute(query)
        return self.select_by_id(item_id)


class User:
    table_name = "user"

    def __init__(self) -> None:
        self.conn = sqlite3.connect("todo.db")

    def __del__(self) -> None:
        self.conn.commit()
        self.conn.close()

    def create(self, name, email):
        query = f"INSERT INTO {self.table_name}(name, email) \
            VALUES('{name}', '{email}')"
        result = self.conn.execute(query)
        return result
