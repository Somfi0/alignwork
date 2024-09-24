import os  
from pathlib import Path

desktop_path = Path.home() / 'pulpit'
test_path = desktop_path / "test"

try: 
    os.makedirs(test_path, exist_ok=True)
    print('zostal utworzony')
except Exception as e:
    print(f"blad {e}")
