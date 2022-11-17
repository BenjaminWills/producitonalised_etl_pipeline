from datetime import datetime as dt

import logging
import pandas as pd
import sqlalchemy as SQLA


class Sqlwrapper:
    """
    Wrapper for sql alchemy.
    """

    def __init__(self,username:str,password:str,host:str,port:str,db_name:str):
        engine = SQLA.create_engine(f"postgresql://{username}:{password}@{host}:{port}/{db_name}")
        self.engine = engine
    
    def read_query(self,query:str) -> pd.DataFrame:
        """
        Executes a query on a table and returns the results as a pandas dataframe.
        """
        con = self.engine.connect()
        results = con.execute(query)
        returns =  results.fetchall()
        con.close()
        return pd.DataFrame(returns)
    
    def drop_table(self,table_name:str,schema_name:str) -> str:
        """
        Will drop specified table.
        """
        con = self.engine.connect()
        con.execute(f"""
        DROP TABLE IF EXISTS {schema_name}.{table_name};
        """)
        con.close()
        return "Table dropped successfully"

    def write_df_to_table(self,data:pd.DataFrame,schema_name:str,table_name:str = None) -> str:
        """
        Will write a pandas df to a postgresql table.
        """
        try:
            self.drop_table(table_name,schema_name)
            data.to_sql(table_name,self.engine,schema = schema_name,index = False)
            return True
        except TypeError as e:
            logging.error(e)
            return False