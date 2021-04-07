import os
import requests
from pathlib import Path
from typing import Dict, Optional
from urllib.parse import urlparse
from tqdm import tqdm


def nonempty_dict(d: dict) -> bool:
    return bool(d)


def filename_from_url(url: str) -> str:
    pr = urlparse(url)
    return os.path.basename(pr.path)


def filesize(f: Path) -> Optional[int]:
    if f.exists():
        return f.stat().st_size
    return None


def download(url: str, dest_folder: Path, chunk_size: int = 1024, overwrite: bool = False) -> Path:
    """
    Downloads a file from url to the specified directory.
    Directory will be created if does not exist.
    Download will be resumed if file parts are found.
    Overwrite can be specified to start download from scratch if anything was downloaded before.
    """
    def resume_headers(start_bytes: int) -> Dict[str, str]:
        return {"Range": f"bytes={start_bytes}-"}

    filename = filename_from_url(url)
    filepath = dest_folder.joinpath(filename)
    dest_folder.mkdir(parents=True, exist_ok=True)
    if overwrite:
        filepath.unlink(missing_ok=True)

    # if file exists, continue download
    current_size = filesize(filepath)
    if current_size is not None:
        r = requests.get(url, stream=True, headers=resume_headers(current_size))
        mode = "ab"
    else:
        r = requests.get(url, stream=True)
        mode = "wb"

    # now save chunk by chunk and show progress
    # below dict is case insensitive, no need to check case
    total_size = int(r.headers.get("Content-Length", "1")) + (current_size or 0)
    with tqdm(
        total=total_size,
        unit="B",
        unit_scale=True,
        desc=str(filepath),
        initial=current_size or 0,
        ascii=True,
    ) as progress:
        with open(filepath, mode) as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    progress.update(len(chunk))
    return filepath
