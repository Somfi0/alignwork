import os 
import random
from pathlib import Path
import shutil

desktop_path = Path.home() / 'OneDrive - Align Technology, Inc/Pulpit'
root_folder = desktop_path / "root"


os.makedirs(root_folder, exist_ok=True)

def file_create(folder_path):
    extensions = ['adf', 'xls', 'csv']
    for ext in extensions:
        file_name = f'file_{random.randint(1, 10000)}.{ext}'
        file_path = folder_path / file_name
        open(file_path, "w").close()
        


num_subfolders = 4
num_inner_subfolders = 10000

for i in range (1, num_subfolders + 1):
    subfolder_path = root_folder / f"folder_{i}"
    os.makedirs(subfolder_path, exist_ok=1)

    for j in range (1, num_inner_subfolders + 1):
        inner_folder_path = subfolder_path / f"folder_{j}"
        os.makedirs(inner_folder_path, exist_ok=True)
        
        file_create(inner_folder_path)

delete_root = input("czy usunac root?: ")

if delete_root == 'y':
    shutil.rmtree(root_folder)
else:
    exit
