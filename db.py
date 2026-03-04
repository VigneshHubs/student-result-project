import mysql.connector
import os

def connect_db():
        return mysql.connector.connect(
                host="localhost",
                user="root",
                password=os.getenv("DB_PASSWORD"),
                database="school"
        )

