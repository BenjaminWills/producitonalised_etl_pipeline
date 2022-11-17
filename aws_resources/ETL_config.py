from helpers.boto3_cloudformation_helper_class import Cloudformation
import os
from dotenv import load_dotenv

load_dotenv(override=True)

ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')

DB_parameters = [
    {
        'ParameterKey': 'DBPassword',
        'ParameterValue': ''
    },
    {
        'ParameterKey': 'DBUsername',
        'ParameterValue': ''
    },
]

ECR_parameters = [
    {
        'ParameterKey': 'ECRName',
        'ParameterValue': 'example_ETL_repository'
    },
]

lambda_parameters = [
    {
        'ParameterKey': 'IngestionScriptURI',
        'ParameterValue': ''
    },
    {
        'ParameterKey': 'CleaningScriptURI',
        'ParameterValue': ''
    },
]

S3_paramaters = [
    {
        'ParameterKey': 'S3BucketName',
        'ParameterValue': 'ETL_bucket'
    },
]
if __name__ == "__main__":
    cloud_formation = Cloudformation(
        ACCESS_KEY_ID,
        SECRET_ACCESS_KEY
    )
    cloud_formation.create_stack(
        stack_name='ETL Stack',
        config_path='aws_resources/ETL_resource_config.yml',
        parameters=[
            *DB_parameters,
            *ECR_parameters,
            *lambda_parameters,
            *S3_paramaters
        ],

    )