import os
import requests
import tarfile
from pathlib import Path


def get_repo_archive(url: str, destination_path: Path) -> Path:
    """
    Given an url and a destination path, retrieve and extract .tar.gz archive
    which contains 'desc' file for each package.
    Each .tar.gz archive corresponds to an Arch Linux repo ('core', 'extra', 'community').

    Args:
        url: url of the .tar.gz archive to download
        destination_path: the path on disk where to extract archive

    Returns:
        a directory Path where the archive has been extracted to.
    """
    # Download the .tar.gz archive
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request failed

    # Save the .tar.gz archive to the destination path
    with open(destination_path / 'archive.tar.gz', 'wb') as f:
        f.write(response.content)

    # Extract the .tar.gz archive
    with tarfile.open(destination_path / 'archive.tar.gz') as tar:
        tar.extractall(path=destination_path)

    # Remove the .tar.gz archive
    os.remove(destination_path / 'archive.tar.gz')

    # Return the directory where the archive has been extracted to
    return destination_path
