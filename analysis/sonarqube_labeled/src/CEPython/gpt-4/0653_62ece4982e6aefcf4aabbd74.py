import os
import tarfile
from typing import Optional, Union
from pathlib import Path, PosixPath
import shutil


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
    # Convert tmp_path to Path object if it's not
    if not isinstance(tmp_path, Path):
        tmp_path = Path(tmp_path)

    # Create a new directory in tmp_path with the name of the archive file
    archive_name = os.path.basename(archive_path).split('.')[0]
    new_dir_path = tmp_path / archive_name
    new_dir_path.mkdir(parents=True, exist_ok=True)

    # Uncompress the archive into the new directory
    with tarfile.open(archive_path) as tar:
        tar.extractall(path=new_dir_path)

    # If filename is specified, move the file to the new directory
    if filename:
        shutil.move(new_dir_path / filename, new_dir_path)

    # Return the path to the new directory as a string
    return str(new_dir_path)
