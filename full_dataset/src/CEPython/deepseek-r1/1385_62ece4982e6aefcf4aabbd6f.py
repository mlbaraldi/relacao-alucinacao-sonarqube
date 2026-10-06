def get_repo_archive(url: str, destination_path: Path) -> Path:
    import os
    import tarfile
    import tempfile
    from pathlib import Path
    import requests
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
    destination_path.mkdir(parents=True, exist_ok=True)

    # Download the archive to a temporary file
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    temp_file.write(chunk)
            temp_file_name = temp_file.name

    try:
        # Extract the archive to the destination path
        with tarfile.open(temp_file_name, mode='r:gz') as tar:
            tar.extractall(path=destination_path)
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_name)

    return destination_path
