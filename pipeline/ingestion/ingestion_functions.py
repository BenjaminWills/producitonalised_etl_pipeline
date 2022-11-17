from helpers.sql_wrapper import Sqlwrapper
import os
from dotenv import load_dotenv

load_dotenv(override=True)

DB_USERNAME  = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST')

sql = Sqlwrapper(
        DB_USERNAME,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_NAME
    )

def ingest_data():
    pass