from helpers.boto3_s3_helper_class import S3
from cleaning_functions import clean
import os
from dotenv import load_dotenv

load_dotenv(override=True)

ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')


def handler(event,context):
    s3 = S3(
        ACCESS_KEY_ID,
        SECRET_ACCESS_KEY
    )
    