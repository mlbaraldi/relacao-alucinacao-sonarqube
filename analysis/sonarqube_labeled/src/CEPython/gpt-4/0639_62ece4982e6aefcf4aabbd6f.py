import requests
from pathlib import Path
import tarfile


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
    # Download the file from the URL
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    # Create the destination directory if it doesn't exist
    destination_path.mkdir(parents=True, exist_ok=True)

    # Create a temporary file to store the downloaded file
    temp_file = destination_path / 'temp.tar.gz'
    with temp_file.open('wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    # Extract the .tar.gz file
    with tarfile.open(temp_file, 'r:gz') as tar:
        tar.extractall(path=destination_path)

    # Delete the temporary file
    temp_file.unlink()

    return destination_path
