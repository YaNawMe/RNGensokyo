import sqlite3

class SQLBase():
    connection = sqlite3.connect('UserDatabase.db', check_same_thread=False)

    @classmethod
    def get_data(cls, table) -> list[tuple]:
        sql_command = """SELECT * FROM :table"""

        data = cls.connection.execute(sql_command, {"table": table})

        return data.fetchall()

    @classmethod
    def insert_data(cls, table_columns: list[str], values: dict[str, object]):
        sql_command = f"""INSERT INTO User{''}(Username, Password) VALUES (:name, :pass)"""
        cls.connection.execute(sql_command, values)
        cls.connection.commit()
    
    @classmethod
    def replace_data(cls, id, username, password):
        sql_command = """REPLACE INTO User(Username, Password) VALUES(:name, :pass) WHERE ID = :id"""
        cls.connection.execute(sql_command, {"id": id, "name": username, "pass": password})
        cls.connection.commit()
    
    @classmethod
    def delete_data(cls, *ids, **kwargs):
        if "delete_all" in kwargs:
            if kwargs["delete_all"]:
                sql_command = """DELETE FROM User"""
                cls.connection.execute(sql_command)
                cls.connection.commit()
        
        else:
            for id in ids:
                sql_command = """DELETE FROM User WHERE ID = :id"""
                cls.connection.execute(sql_command, {"id": id})
                cls.connection.commit()