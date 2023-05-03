import pathlib
from typing import Tuple


def create_gcloud_vm_docker_template(
    target_dir: str,
    base_docker_image: str,
    package_dependencies: Tuple[str],
    gcloud_artifact_registry_domain: str,
    gcloud_project_name: str,
    gcloud_repository_id: str,
    docker_image_name: str,
) -> None:
    """Creates a folder containing the files necessary to quickly build a python docker container to run on a google cloud Virtual Machine

    The following structure is created in the target directory:
    /target_dir/
        Dockerfile
        main.py
        requirements.txt

    Parameters
    ----------
    target_dir : str
        The path to the local directory in which the folder (and contents) should be created
    base_docker_image : str
        The base image to use for the docker container (e.g. "python:3.10-slim")
    package_dependencies : Tuple[str]
        A tuple containing the package dependencies (these are written to requirements.txt)
    gcloud_artifact_registry_domain : str
        The domain of the google cloud artifact registry (e.g. "europe-west2")
    gcloud_project_name : str
        The name of the google cloud project in which the docker image will be stored
    gcloud_repository_id : str
        The name of the google cloud artifact repository in which the docker image will be stored
    docker_image_name : str
        The desired name for the docker image

    Example Usage
    -------------
    >>> import joes_giant_toolbox.google_cloud
    >>> joes_giant_toolbox.google_cloud.create_gcloud_vm_docker_template(
    ...     target_dir="temp/docker_test/",
    ...     base_docker_image="python:3.10-slim",
    ...     package_dependencies=["numpy==1.24.1","tqdm"],
    ...     gcloud_artifact_registry_domain="europe-west2",
    ...     gcloud_project_name="my_project_name",
    ...     gcloud_repository_id="my_docker_repo_name",
    ...     docker_image_name="my_docker_image_name",
    ... )
    >>> os.listdir("temp/docker_test")
    ['requirements.txt', 'Dockerfile', 'main.py']
    """
    # create target directory if it does not exist #
    pathlib.Path(target_dir).mkdir(parents=True, exist_ok=True)

    # create files in target directory #
    with open(f"{target_dir}/main.py", "w") as f:
        f.write(
            """
# set up google cloud logging #
import logging
import google.cloud.logging

logging_client = google.cloud.logging.Client()
logging_client.setup_logging()

logging.info("this message will appear in google cloud logging")

# write your python code here #
"""
        )
    with open(f"{target_dir}/requirements.txt", "w") as f:
        for x in package_dependencies:
            f.write(x + "\n")
    with open(f"{target_dir}/Dockerfile", "w") as f:
        newline_char = "\n"
        f.write(
            f"""
# gcloud auth configure-docker {gcloud_artifact_registry_domain}-docker.pkg.dev
# cd {target_dir}
# docker buildx build --platform linux/amd64 --tag {gcloud_artifact_registry_domain}-docker.pkg.dev/{gcloud_project_name}/{gcloud_repository_id}/{docker_image_name} .
# docker push {gcloud_artifact_registry_domain}-docker.pkg.dev/{gcloud_project_name}/{gcloud_repository_id}/{docker_image_name}

FROM {base_docker_image}

# copy all code in folder to the container #
WORKDIR /{target_dir}
COPY . ./

# install packages #
RUN pip install --no-cache-dir -r requirements.txt

# execute python script #
CMD ["python","main.py"]
"""
        )
