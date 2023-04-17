from typing import List
import google.cloud.bigquery
import google.cloud.storage
import pandas as pd


def delete_file_in_gcloud_bucket(
    bucket_name: str, file_name: str, verbose: bool = True
) -> None:
    """Delete a file which is in a google cloud bucket

    Notes
    -----
    This code is mostly taken from the Google Cloud documentation https://cloud.google.com/storage/docs/deleting-objects#client-libraries

    Parameters
    ----------
    bucket_name: str
        The name of the bucket containing the file
    file_name: str
        The name of the file to be deleted
    verbose: bool, optional (default=True)
        Whether to print status messages about the process

    Example Usage
    -------------
    >>> delete_file_in_gcloud_bucket(bucket_name="output_bucket", file_name="users.json")
    Deleted file from google cloud bucket gs://output_bucket/users.json
    >>> delete_file_in_gcloud_bucket(bucket_name="output_bucket", file_name="2023/01/users.json")
    Deleted file from google cloud bucket gs://output_bucket/2023/01/users.json
    """
    storage_client = google.cloud.storage.Client()
    bucket_obj = storage_client.bucket(bucket_name)
    file_blob = bucket_obj.blob(file_name)

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to delete is aborted if the object's
    # generation number does not match your precondition.
    generation_match_precondition = None
    file_blob.reload()  # Fetch blob metadata to use in generation_match_precondition.
    generation_match_precondition = file_blob.generation
    file_blob.delete(if_generation_match=generation_match_precondition)
    if verbose:
        print(f"Deleted file from google cloud bucket gs://{bucket_name}/{file_name}")


def download_file_from_gcloud_bucket_to_python(
    bucket_name: str, file_name: str
) -> google.cloud.storage.blob.Blob:
    """
    Read a file from a google cloud bucket into python memory

    Parameters
    ----------
    bucket_name: str
        The name of the google cloud bucket
    file_name: str
        The name of the file to be downloaded

    Returns
    -------
    google.cloud.storage.blob.Blob
        A wrapper around Cloud Storage's concept of an Object
        See "Example Usage" (below) for examples of how to interact with this object

    Example Usage
    -------------
    >>> import json
    >>> import pandas as pd
    >>> import google.cloud.storage
    >>> with download_file_from_gcloud_bucket_to_python(
    ...         bucket_name="my-bucket-name", file_name="my_json_file.json"
    ...     ).open("r") as f:
    ...         my_json = json.load(f)
    >>> with download_file_from_gcloud_bucket_to_python(
    ...            bucket_name="my-bucket-name", file_name="my_text_file.txt"
    ...     ).open("r") as f:
    ...         my_text = f.read()
    >>> with download_file_from_gcloud_bucket_to_python(
    ...         bucket_name="my-bucket-name", file_name="my_table.csv"
    ...     ).open("r") as f:
    ...         my_table = pd.read_csv(f)
    """

    bucket = google.cloud.storage.Client().bucket(bucket_name)
    blob = bucket.blob(file_name)

    return blob


def list_files_in_gcloud_bucket(bucket_name: str, prefix: str = None) -> List[str]:
    """
    Returns a list of the files (filenames) present in a google cloud bucket

    Parameters
    ----------
    bucket_name: str
        The name of the google cloud bucket
    prefix: str, optional (default=None)
        If present, only returns files whose path starts with the given prefix

    Returns
    -------
    List[str]
        List of filenames in the google cloud bucket (file pathes)
    """
    storage_client = google.cloud.storage.Client()
    if prefix is not None:
        blobs = storage_client.list_blobs(bucket_name, prefix=prefix)
    else:
        blobs = storage_client.list_blobs(bucket_name)
    all_filenames = []
    for blob in blobs:
        all_filenames.append(blob.name)

    return all_filenames


def write_pandas_df_to_google_bigquery_table(
    pandas_df: pd.DataFrame, bigquery_table_path: str, column_schema: list
) -> None:
    """
    Writes a pandas dataframe to a table on Google BigQuery

    Parameters
    ----------
    pandas_df: pandas.DataFrame
        Table to be written to BigQuery
    bigquery_table_path: str
        Path to destination table e.g. "project_name.dataset_name.table_name"
    column_schema: list of google.cloud.bigquery.enums.SqlTypeNames objects
        A list of column data types, informing BigQuery of the data type of each column (refer to the example below)
        This list is passed to the parameter "schema" in the function bigquery.LoadJobConfig()

    Example Usage
    -------------
    >>> import pandas as pd
    >>> import google.cloud.bigquery
    >>> example_df = pd.DataFrame(
    ...   {
    ...     "string_column": ["a","b","c"],
    ...     "integer_column": [-100,0,100],
    ...     "float_column": [3.14159,6.9,4.2],
    ...   }
    ... )
    >>> write_pandas_df_to_google_bigquery(
    ...   pandas_df = example_df,
    ...   bigquery_table_path = "project_name.dataset_name.table_name",
    ...   column_schema = [
    ...     google.cloud.bigquery.SchemaField("string_column", google.cloud.bigquery.enums.SqlTypeNames.STRING),
    ...     google.cloud.bigquery.SchemaField("integer_column", google.cloud.bigquery.enums.SqlTypeNames.INT64),
    ...     google.cloud.bigquery.SchemaField("float_column", google.cloud.bigquery.enums.SqlTypeNames.FLOAT64),
    ...   ],
    ... )
    """
    client = google.cloud.bigquery.Client()
    job = client.load_table_from_dataframe(
        pandas_df,
        bigquery_table_path,
        job_config=google.cloud.bigquery.LoadJobConfig(schema=column_schema),
    )
    job.result()  # wait for the job to complete
