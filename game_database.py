import sqlite3

class SQLBase():
    connection = sqlite3.connect("UserDatabase.db", check_same_thread=False)

    @classmethod
    def get_data(cls, table) -> list[tuple]:
        sql_command = f"""SELECT * FROM {table}"""

        data = cls.connection.execute(sql_command)

        return data.fetchall()

    @classmethod
    def insert_data(cls, table, table_columns: list[str], column_values: dict):
        key_value = [(':' + key) for key in column_values.keys()]

        sql_command = f"""INSERT INTO {table}({','.join(table_columns)}) VALUES({','.join(key_value)})"""

        cls.connection.execute(sql_command, column_values)

        cls.connection.commit()
    
    @classmethod
    def replace_data(cls, table, table_columns: list[str], column_values: dict, column_check: str, check_value: str):
        key_value = [(':' + key) for key in column_values.keys()]

        sql_command = f"""REPLACE INTO {table}({','.join(table_columns)}) VALUES({','.join(key_value)}) WHERE :column = :check"""
        
        column_values[column_check] = check_value

        cls.connection.execute(sql_command, column_values)
        cls.connection.commit()
    
    @classmethod
    def delete_data(cls, table, *ids, **kwargs):
        if "delete_all" in kwargs:
            if kwargs["delete_all"]:
                sql_command = f"""DELETE FROM {table}"""

                cls.connection.execute(sql_command)
                cls.connection.commit()

                return
            
        for id in ids:
            sql_command = f"""DELETE FROM {table} WHERE :column = :check"""
            cls.connection.execute(sql_command, {"id": id})
            cls.connection.commit()


class SQLLogin:
    @classmethod
    def get_data(cls):
        SQLBase.get_data("UserLogin")
    
    @classmethod
    def insert_data(cls, username, password):
        SQLBase.insert_data("UserLogin", ["Username", "Password"], {"name": username, "pass": password})
    
    @classmethod
    def replace_data(cls, username, password, id):
        SQLBase.replace_data("UserLogin", ["Username", "Password"], {"name": username, "pass": password}, "ID", id)
    
    @classmethod
    def delete_data(cls, *ids, **kwargs):
        SQLBase.delete_data("UserLogin", *ids, **kwargs)

class SQLUserData:
    @classmethod
    def get_data(cls):
        SQLBase.get_data("UserData")
    
    @classmethod
    def insert_data(cls, username, password):
        SQLBase.insert_data(["Username", "Password"], {"name": username, "pass": password})
    
    @classmethod
    def replace_data(cls, username, password, id):
        SQLBase.replace_data(["Username", "Password"], {"name": username, "pass": password}, "ID", id)
    
    @classmethod
    def delete_data(cls, table, *ids, **kwargs):
        SQLBase.delete_data(table, *ids, **kwargs)