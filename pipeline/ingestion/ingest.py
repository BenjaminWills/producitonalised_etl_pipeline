from helpers.boto3_s3_helper_class import S3
from helpers.sql_wrapper import Sqlwrapper
import os
from dotenv import load_dotenv
import logging

from ingestion_functions import load_data_to_df,ingest_data

load_dotenv(override=True)

DB_USERNAME  = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST')


ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')

BUCKET_NAME = 'string'
SCHEMA_NAME = 'string'
TABLE_NAME = 'string'

logger = logging.getLogger()

def handler(event,context):
    s3 = S3(
    ACCESS_KEY_ID,
    SECRET_ACCESS_KEY,
    AWS_REGION
    )
    sql = Sqlwrapper(
        DB_USERNAME,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_NAME
    )
    logger.info('Reading data...')
    data = ingest_data(s3,BUCKET_NAME)
    logger.info('Data read...')
    load_data_to_df(sql,data,SCHEMA_NAME,TABLE_NAME)
    logger.info(f'Data successfully inputted into {DB_NAME}.{SCHEMA_NAME}.{TABLE_NAME}')