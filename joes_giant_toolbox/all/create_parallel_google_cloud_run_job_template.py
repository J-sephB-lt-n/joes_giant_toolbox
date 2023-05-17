"""This script defines the function create_parallel_google_cloud_run_job_template()"""

import pathlib
from typing import Any, Dict, List


# pylint: disable-msg=too-many-arguments
def create_parallel_google_cloud_run_job_template(
    gcp_region: str,
    cloud_run_job_name: str,
    instruction_file_bucket_name: str,
    instruction_file_path: str,
    pre_task_code: List[str],
    task_code: List[str],
    cloud_run_job_params: Dict[str, Any],
    requirements_list: List[str],
    target_dir: str,
) -> None:
    """Populates a folder with code for creating a Google Cloud Run Job
    (for running the same task in parallel)

    Parameters
    ----------


    Example Usage
    -------------
    >>> import random
    >>> import string
    >>> import joes_giant_toolbox.google_cloud
    >>> # create list of names to process (in parallel) using a Cloud Run job #
    >>> names_to_process: list = [
    ...    "".join(random.choices(string.ascii_lowercase, k=8)) for name in range(100)
    ... ]
    >>> names_to_process
    ['rhfdlmqq', 'hjogakjd', 'cfbhrhfj', ...]
    >>> joes_giant_toolbox.google_cloud.upload_file_python_to_gcloud_bucket(
    ...     contents_str = "\n".join(names_to_process),
    ...     bucket_name="cloud_run_jobs_test",
    ...     filename_on_bucket="names_to_process.txt",
    ...     file_type="text"
    ... )
    >>> os.chdir(target_dir)
    >>> subprocess.run(["bash", "create_cloud_run_job.sh"])
    ...
    """
    # create target directory if it does not exist #
    pathlib.Path(target_dir).mkdir(parents=True, exist_ok=True)

    procfile_contents: str = """
# Buildpacks require a web process to be defined
# but this process will not be used
web: echo "no web"
python: python
"""

    requirements_txt_contents: str = ""
    for pkg in requirements_list + [
        "click",
        "google-auth",
        "google-cloud-logging",
        "google-cloud-storage",
    ]:
        requirements_txt_contents += f"{pkg}\n"

    main_py_contents: str = f"""
import logging
import math
import os
import time\n
from typing import Final
import click
import google.auth
import google.cloud.logging
import google.cloud.storage\n
# connect to google cloud logging and storage services #
gcp_logging_client = google.cloud.logging.Client()
gcp_storage_client = google.cloud.storage.Client()\n
_, PROJECT_ID = google.auth.default()
BATCH_ID: Final = int(os.environ.get("CLOUD_RUN_TASK_INDEX", 0))
N_BATCHES: Final = int(os.environ.get("CLOUD_RUN_TASK_COUNT", 1))\n
gcp_logging_client.setup_logging()\n
# user-specified pre-task code -------------------------------------------- #
{chr(10).join(pre_task_code)}
# ------------------------------------------------------------------------- #\n
@click.command()
@click.argument("input_bucket_name")
@click.argument("file_path_on_input_bucket")
def process(input_bucket_name, file_path_on_input_bucket):
    batch_start_time = time.time()
    logging.info(
        f"STARTED batch {{BATCH_ID}} of {{N_BATCHES}}\\n"
        f"Instructions list is gs://{{input_bucket_name}}/{{file_path_on_input_bucket}}\\n"
    )
    gcp_bucket = gcp_storage_client.bucket(input_bucket_name)
    gcp_bucket_file = gcp_bucket.blob(file_path_on_input_bucket)\n
    file_contents: str = gcp_bucket_file.download_as_string().decode("utf-8")
    items_list: list = file_contents.split("\\n")
    batch_size: int = math.ceil(len(items_list) / N_BATCHES)
    batch_start_idx: int = batch_size * BATCH_ID
    batch_end_idx: int = batch_start_idx + batch_size\n
    logging.info(
        f"This batch ({{BATCH_ID}}) processing items {{batch_start_idx}} to {{batch_end_idx-1}}"
    )\n
    for x in items_list[batch_start_idx:batch_end_idx]:
        # user-specified task code --------------------------------------------- #
{chr(10).join(['        '+x for x in task_code])}
        # ---------------------------------------------------------------------- #\n
    batch_end_time = time.time()
    logging.info(
        f"COMPLETED: batch {{BATCH_ID}} of {{N_BATCHES}}\\n"
        f"..from instruction list gs://{{input_bucket_name}}/{{file_path_on_input_bucket}}\\n"
        f"Number of minutes taken: {{(batch_end_time-batch_start_time)/60:,.5f}}"
    )\n
if __name__=="__main__":
    process()
"""

    create_cloud_run_job_sh_contents: str = f"""
GCP_PROJECT_ID=$(gcloud config get project)
GCP_REGION={gcp_region}
GCP_CLOUD_RUN_JOB_NAME={cloud_run_job_name}
DOCKER_IMAGE_PATH=gcr.io/${{GCP_PROJECT_ID}}/${{GCP_CLOUD_RUN_JOB_NAME}}
INSTRUCTION_FILE_BUCKET_NAME={instruction_file_bucket_name}
INSTRUCTION_FILE_PATH={instruction_file_path}\n
echo "Setting gcloud to use region=$GCP_REGION for Cloud Run"
gcloud config set run/region ${{GCP_REGION}}\n
echo "...done"
echo "Enabling required gcloud services"
gcloud services enable run.googleapis.com cloudbuild.googleapis.com
echo "...done"
echo "Building process docker container and pushing to gcloud"
gcloud builds submit --pack image=${{DOCKER_IMAGE_PATH}}
echo "...done"
echo "Deleting cloud run job (if it already exists)"
gcloud beta run jobs delete ${{GCP_CLOUD_RUN_JOB_NAME}} --quiet
echo "Executing Cloud Run Job..."
echo "  ...with $NUM_BATCHES batches"
echo "  ...instructions file is gs://$INSTRUCTION_FILE_BUCKET_NAME/$INSTRUCTION_FILE_PATH"
gcloud beta run jobs create \\
${{GCP_CLOUD_RUN_JOB_NAME}} \\
--execute-now \\
--image ${{DOCKER_IMAGE_PATH}} \\
--command python \\
--args main.py,${{INSTRUCTION_FILE_BUCKET_NAME}},${{INSTRUCTION_FILE_PATH}} \\
{" ".join([f"{k} {cloud_run_job_params[k]} " for k in cloud_run_job_params])}
echo "...done"
"""
    with open(f"{target_dir}/Procfile", "w", encoding="utf-8") as file:
        file.write(procfile_contents)

    with open(f"{target_dir}/main.py", "w", encoding="utf-8") as file:
        file.write(main_py_contents)

    with open(f"{target_dir}/create_cloud_run_job.sh", "w", encoding="utf-8") as file:
        file.write(create_cloud_run_job_sh_contents)

    with open(f"{target_dir}/requirements.txt", "w", encoding="utf-8") as file:
        file.write(requirements_txt_contents)


if __name__ == "__main__":
    import os
    import subprocess

    code_output_dir: str = f"{pathlib.Path.home()}/Documents/temp/define_cloud_run_job/"
    create_parallel_google_cloud_run_job_template(
        pre_task_code=[
            "import random",
            "import time",
            "import joes_giant_toolbox.google_cloud",
        ],
        task_code=[
            "joes_giant_toolbox.google_cloud.upload_file_python_to_gcloud_bucket(",
            "   contents_str=str(random.uniform(0,1))[:7], # write random number to file",
            '   bucket_name="cloud_run_jobs_test",',
            '   filename_on_bucket=f"completed_files/{x}.txt",',
            '   file_type="text"',
            ")",
            "time.sleep( random.uniform(1,5) )",
        ],
        target_dir=code_output_dir,
        gcp_region="europe-west2",
        cloud_run_job_name="temp-once-off-job",
        instruction_file_bucket_name="cloud_run_jobs_test",
        instruction_file_path="names_to_process.txt",
        requirements_list=[
            "joes-giant-toolbox>=0.2.23",
            "google-cloud-bigquery",
            "google-cloud-storage",
            "pandas",
        ],
        cloud_run_job_params={
            "--tasks": 10,
            "--max-retries": 3,
            "--task-timeout": "5m30s",
        },
    )
    os.chdir(code_output_dir)
    subprocess.run(["bash", "create_cloud_run_job.sh"], check=True)
