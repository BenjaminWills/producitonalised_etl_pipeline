from helpers.boto3_s3_helper_class import S3
from helpers.sql_wrapper import Sqlwrapper
import os
from dotenv import load_dotenv

load_dotenv(override=True)

ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')





def handler(event,context):
    s3 = S3(
        ACCESS_KEY_ID,
        SECRET_ACCESS_KEY,
        AWS_REGION
    )
    
    contents = s3.list_bucket_contents('ETL_bucket')