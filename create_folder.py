import os 
import random
from pathlib import Path
import shutil
import time

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
num_inner_subfolders = 8000

for i in range (1, num_subfolders + 1):
    subfolder_path = root_folder / f"folder_{i}"
    os.makedirs(subfolder_path, exist_ok=1)

    for j in range (1, num_inner_subfolders + 1):
        inner_folder_path = subfolder_path / f"old_folder_{j}"
        os.makedirs(inner_folder_path, exist_ok=True)
        
        file_create(inner_folder_path)
        
print("Pierwsza pratia folderow zostala utworzona")

print("odliczam dziesiec minut przed stworzeniem nowej partii")
time.sleep(15*60)

request = input("Czy stworzyc nowa partie folderow z plikami?: ")

new_folders = 2000

if request == 'yes':
    for i in range(1, num_subfolders +1):
        subfolder_path = root_folder / f"folder_{i}"

        for j in range (1, new_folders + 1):
            new_folder_path = subfolder_path / f"new_folders_{j}"
            os.makedirs(new_folder_path, exist_ok=True)

            file_create(new_folder_path)

delete_root = input("czy usunac root?: ")

if delete_root == 'y':
    start_time = time.time()
    shutil.rmtree(root_folder)
    stop_time = time.time()
    print(f"Czas usuwania calego root wynosi: {stop_time - start_time}")
    
else:
    exit
