def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
    import os
    from pathlib import Path
    from typing import Optional, Union
    import zipfile
    import tarfile
    tmp_dir = Path(tmp_path) if isinstance(tmp_path, str) else tmp_path
    if filename is None:
        archive_basename = Path(archive_path).name
        name = archive_basename
        while True:
            root, ext = os.path.splitext(name)
            if not ext:
                break
            name = root
        dir_name = name
    else:
        dir_name = filename
    target_dir = tmp_dir / dir_name
    target_dir.mkdir(parents=True, exist_ok=True)
    
    if zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(target_dir)
    elif tarfile.is_tarfile(archive_path):
        with tarfile.open(archive_path, 'r:*') as tar:
            tar.extractall(path=target_dir)
    else:
        raise ValueError(f"Unsupported archive format: {archive_path}")
    
    return str(target_dir)
