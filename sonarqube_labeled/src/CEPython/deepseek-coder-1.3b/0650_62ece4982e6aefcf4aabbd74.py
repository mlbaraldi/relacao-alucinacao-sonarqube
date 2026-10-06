import tarfile
from pathlib import Path
from typing import Optional, Union
from posixpath import PosixPath


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
    if not Path(archive_path).exists():
        raise FileNotFoundError(f"Archive file {archive_path} not found")

    tmp_dir = Path(tmp_path) / "repo"
    tmp_dir.mkdir(parents=True, exist_ok=True)

    with tarfile.open(archive_path, "r:gz") as tar:
        tar.extractall(path=str(tmp_dir))

    repo_url = str(tmp_dir / (filename if filename else tar.getmembers()[0].name))
    return repo_url
