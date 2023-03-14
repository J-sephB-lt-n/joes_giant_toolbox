from google.cloud import bigquery
import pandas as pd


def query_bigquery_to_pandas_df(query_str: str) -> pd.DataFrame:
    """Runs a query on Google BigQuery and writes the result into a local pandas.DataFrame

    parameters
    ----------
    query_str
        A string containing the query to run on Google BigQuery

    returns
    -------
    pandas.DataFrame
        A pandas dataframe

    example usage
    -------------
    >>> "SELECT COUNT(*) AS n_rows, COUNT(DISTINCT user_id) AS n_unique_user_id FROM `project_name.dataset_name.table_name`"
    69420
    """
    client = bigquery.Client()

    return client.query(query_str).result().to_dataframe()
