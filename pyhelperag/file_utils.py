import os
import shutil
from pathlib import Path

def find_files_by_ext(folder, ext):
    return list(Path(folder).rglob(f"*.{ext}"))

def get_file_size_readable(path):
    size = os.path.getsize(path)
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def backup_file(file_path, backup_dir="backups"):
    Path(backup_dir).mkdir(exist_ok=True)
    shutil.copy(file_path, Path(backup_dir) / Path(file_path).name)
