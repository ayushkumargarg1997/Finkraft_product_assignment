from fastapi import FastAPI, Body, Depends
import psycopg2
import configparser
import os
import logging

logging.basicConfig(level=logging.DEBUG, filename="app.log")
logger = logging.getLogger(__name__)


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "config.ini"))

postgresql_config = config["postgresql"]
db_host = postgresql_config["host"]
db_port = postgresql_config["port"]
db_name = postgresql_config["database"]
db_user = postgresql_config["username"]
db_password = postgresql_config["password"]

# Function to create a database connection
def create_connection():
    try:
        return psycopg2.connect(
            host=db_host,  # or use the IP address of the database container
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password,
        )
    except psycopg2.Error as e:
        logger.info(f"Failed to connect to the database: {e}")
        raise

async def select_query(query, params=None):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute(query, params)
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result
    except psycopg2.Error as e:
        logger.error(f"Error in retrieving data: {e}")
        return False
        # return {"error": f"Failed to execute query: {e}"}
    

async def insert_query(query, params=None):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute(query, params)
        conn.commit()
        serial_key_id = cursor.fetchone()

        logger.info("Data inserted successfully!")
        cursor.close()
        conn.close()

        return serial_key_id[0]

    except psycopg2.Error as e:
        logger.error(f"Error inserting data: {e}")
        return False
        # return {"error": f"Failed to execute query: {e}"}

