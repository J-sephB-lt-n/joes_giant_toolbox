import google.cloud.storage


def move_or_rename_file_in_gcloud_bucket(
    source_bucket_name: str,
    source_filename: str,
    destination_bucket_name: str,
    destination_filename: str,
    verbose: bool = True,
) -> None:
    """Move or rename a file which is in a google cloud bucket (which includes moving it to a different bucket)

    Notes
    -----
    This code is stolen from the google cloud documentation (https://cloud.google.com/storage/docs/copying-renaming-moving-objects#storage-move-object-python)

    Parameters
    ----------
    source_bucket_name: str
        Bucket name that file is currently in
    source_filename: str,
        Current name of the file in the source bucket
    destination_bucket_name: str
        Name of bucket that you want to move file to (can be the same as [source_bucket_name])
    destination_filename: str
        Desired name of the file in the destination bucket
    """
    storage_client = google.cloud.storage.Client()
    source_bucket = storage_client.bucket(source_bucket_name)
    source_blob = source_bucket.blob(source_filename)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_filename
    )
    source_bucket.delete_blob(source_filename)

    print(
        f"File {source_blob.name} in bucket {source_bucket.name} moved to blob {blob_copy.name} in bucket {destination_bucket.name}"
    )