import os
import tarfile
import urllib.request


def get_repo_archive(url: str, destination_path: Path) -> Path:
    # Download the .tar.gz archive
    response = urllib.request.urlopen(url)
    data = response.read()

    # Extract the archive to the destination path
    with tarfile.open(fileobj=data, mode="r:gz") as tar:
        tar.extractall(destination_path)

    # Return the path to the extracted directory
    return destination_path / os.path.basename(url).split(".tar.gz")[0]
