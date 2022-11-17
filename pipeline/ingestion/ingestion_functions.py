from helpers.boto3_s3_helper_class import S3
from helpers.sql_wrapper import Sqlwrapper
import pandas as pd


def ingest_data(s3:S3,bucket_name:str) -> pd.DataFrame:
    """Ingests the most recently uploaded file in the s3 bucket.

    Parameters
    ----------
    bucket_name : str

    Returns
    -------
    pd.DataFrame
        DF form of the CSV within the bucket
    """
    most_recent_file_name = s3.list_bucket_contents(bucket_name)[-1]['Name']
    return pd.read_csv(f's3://{most_recent_file_name}')

def load_data_to_df(sql:Sqlwrapper,dataframe:pd.DataFrame,schema_name:str,table_name:str) -> bool:
    """Loads a dataframe to an sql table.

    Parameters
    ----------
    sql : Sqlwrapper
    dataframe : pd.DataFrame
    schema_name : str
    table_name : str

    Returns
    -------
    bool
        Response as to whether the function was successful or not
    """
    response = sql.write_df_to_table(dataframe,schema_name,table_name)
    return response