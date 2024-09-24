import os 
import random
from pathlib import Path
import shutil

desktop_path = Path.home() / 'Desktop'
root_path = desktop_path / "root"

try:
    os.makedirs(root_path, exist_ok=True)
    print("root zostal utworzony")
except Exception as e:
    print('nie utworzylo bo {e}')

num_subfolders = 4
num_inner_folders = 10000

for i in range (1, num_subfolders +1):
    subfolder_path = root_path / f'sub_folder_{i}'
    os.makedirs(subfolder_path, exist_ok=True)

    for j in range (1, num_inner_folders + 1):
        inner_folder_path = subfolder_path / f'inner_fodler_{j}'
        os.makedirs(inner_folder_path, exist_ok=True)


delete_root = input("Usunac root? jesli tak to wprowadz y: ")

if delete_root == 'y':
    shutil.rmtree(root_path)
else: 
    exit

