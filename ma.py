import os
import time
import shutil
from datetime import datetime, timedelta
from pathlib import Path

def get_oldest_date():
    six_month_old = datetime.now() - timedelta(minutes=10)
    return six_month_old.timestamp()

def is_older(file_stat):
    creation_time = file_stat.st_ctime
    acces_time = file_stat.st_atime
    oldest_date = get_oldest_date()

    return creation_time < oldest_date or acces_time <oldest_date

def clean_folder(root_path):
    for root, dirs, files in os.walk(root_path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_stat = os.stat(file_path)
                if is_older(file_stat):
                    print(f"usuwam plik:{file_path}")
                    os.remove(file_path)
            except Exception as e:
                print(f'blad usuwania pliku {file_path}: {e}')
    
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                if not os.listdir(dir_path):
                    dir_stat = os.stat(dir_path)
                    if is_older(dir_stat):
                        print(f"usuwanie pustego folderu ktory jest starszy od 6 msc: {dir_path}")
                        shutil.rmtree(dir_path)
            except Exception as e:
                print(f"wystapil blad z folderem {dir_path} {e}")




desktop_path = Path.home() / 'OneDrive - Align Technology, Inc/Pulpit'
root_path = desktop_path / "root"

start_time = time.time()
clean_folder(root_path)
end_time = time.time()
print(f"calosciowe usuniecie wszystkiego wynioslo: {end_time-start_time}")