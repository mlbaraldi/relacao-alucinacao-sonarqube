import os
import tarfile
from typing import Optional, Union, PosixPath
from pathlib import Path


def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
    """
    Given an existing archive_path, uncompress it.
    Returns a file repo url which can be used as origin url.

    This does not deal with the case where the archive passed along does not exist.
    """
    # Convert tmp_path to Path object
    tmp_path = Path(tmp_path)

    # Create the temporary directory
    repo_path = tmp_path / 'repo'
    repo_path.mkdir(parents=True, exist_ok=True)

    # Uncompress the archive
    with tarfile.open(archive_path, 'r') as tar:
        tar.extractall(path=repo_path)

    # If a filename is provided, return the path to that file
    if filename:
        return str(repo_path / filename)

    # Otherwise, return the path to the uncompressed directory
    return str(repo_path)
