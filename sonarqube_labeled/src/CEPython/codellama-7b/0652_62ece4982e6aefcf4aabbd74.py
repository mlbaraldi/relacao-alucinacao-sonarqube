import os
import shutil
import tarfile
import tempfile


def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
    # Create a temporary directory to extract the archive
    tmp_dir = tempfile.mkdtemp(dir=tmp_path)

    # Extract the archive to the temporary directory
    with tarfile.open(archive_path, "r:gz") as tar:
        tar.extractall(tmp_dir)

    # Find the first file in the temporary directory
    if filename is None:
        for root, dirs, files in os.walk(tmp_dir):
            if files:
                filename = files[0]
                break

    # Create a file repository from the extracted file
    repo_url = "file://" + os.path.join(tmp_dir, filename)

    # Clean up the temporary directory
    shutil.rmtree(tmp_dir)

    return repo_url
