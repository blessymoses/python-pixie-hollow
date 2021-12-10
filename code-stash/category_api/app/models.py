import sqlite3
import pymysql


class Schema:
    def __init__(self) -> None:
        self.conn = self.conn = pymysql.connect(
            host=rds_host, user=name, passwd=password, db=db_name
        )
        # self.create_category_table()

    def create_category_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS 'category'(
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


class CategoryModel:
    table_name = "category"

    def __init__(self) -> None:
        self.conn = self.conn = pymysql.connect(
            host=rds_host, user=name, passwd=password, db=db_name
        )

    def __del__(self) -> None:
        self.conn.commit()
        self.conn.close()

    def select(self, where_clause=""):
        columns = ["id", "title", "description", "due_date", "is_done", "is_deleted"]
        query = (
            f"SELECT {', '.join(columns)} \
            FROM {self.table_name} WHERE is_deleted != {1} "
            + where_clause
        )
        print(query)
        result_set = self.conn.execute(query).fetchall()
        # print(result_set)
        return result_set

    def select_by_category(self, _id):
        # where_clause = f"AND id = {_id}"
        # return self.select(where_clause)
        pass

    def update(self, item_id, update_category):
        query = f"UPDATE {self.table_name} SET category = {update_category} \
            WHERE id = {item_id}"
        self.conn.execute(query)
