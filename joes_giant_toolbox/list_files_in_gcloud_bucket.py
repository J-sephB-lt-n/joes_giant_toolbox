from google.cloud import storage


def list_files_in_gcloud_bucket(project_name: str, bucket_name: str) -> list:
    """
    Returns a list of the files present in a specified google cloud bucket

    Parameters
    ----------
    project_name: str
        The name of the google cloud project containing the bucket of interest
    bucket_name: str
        The name of the google cloud bucket

    Returns
    -------
    list
        List of files in the bucket (file pathes)
    """
    storage_client = storage.Client(project=project_name)
    blobs = storage_client.list_blobs(bucket_name)
    all_filenames = []
    for blob in blobs:
        all_filenames.append(blob.name)

    return all_filenames
