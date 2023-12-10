import sqlite3
from utilities.common_functions import *


def connect_database():
    parent_path = get_parent_framework_path()
    get_location = parent_path + "\\base_datas\\pythonsqlite.db"
    conn = sqlite3.connect(get_location)
    cursor = conn.cursor()
    return conn, cursor


def read_data_from_database(table_name, column_name=None, condition=None):
    conn, cursor = connect_database()
    query = ""
    if column_name is None:
        query = "SELECT * FROM " + table_name
    else:
        query = "SELECT " + column_name + " FROM " + table_name
    if condition is not None:
        query = query + " WHERE " + condition
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data


def write_data_to_database(table_name, column_name, value):
    conn, cursor = connect_database()
    query = "INSERT INTO " + table_name + "(" + column_name + ") VALUES('" + value + "')"
    cursor.execute(query)
    conn.commit()
    conn.close()