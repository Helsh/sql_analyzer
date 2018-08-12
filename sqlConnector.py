#!/usr/bin/env python3
import psycopg2

DB_CONNECTION_NAME = "dbname=news"


class SQLConnector:
    def __init__(self):
        self.db_connection = psycopg2.connect(DB_CONNECTION_NAME)
        self.cursor = self.db_connection.cursor()

    def fetchData(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def closeConnection(self):
        self.db_connection.close()
