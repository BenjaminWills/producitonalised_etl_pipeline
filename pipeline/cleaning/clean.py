from helpers.boto3_s3_helper_class import S3
from helpers.sql_wrapper import Sqlwrapper
from cleaning_functions import clean
import os
from dotenv import load_dotenv

load_dotenv(override=True)

ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')

DB_USERNAME  = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST')



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
    