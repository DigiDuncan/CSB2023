import requests
import zipfile
import os
from pathlib import Path
import tkinter as tk
from tqdm import tqdm
from tkinter import filedialog

CSBIII = R"https://dl.dropboxusercontent.com/scl/fi/1liq34h0e612kgegteta8/CSBIII-1.0RC2-pc.zip?rlkey=dwrcsj706ok135ihuvoz9163e&dl=0"

root = tk.Tk()
root.withdraw()

def main():
    print("Please select an output directory:")
    directory_path = filedialog.askdirectory()
    output_path = Path(directory_path) / "CSBIII"
    zip_path = output_path / "temp.zip"
    output_path.mkdir(parents = True)

    print("Downloading!")
    response = requests.get(CSBIII, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1KB
    progress_bar = tqdm(total = total_size_in_bytes, unit='iB', unit_scale=True)
    with open(zip_path, 'xb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("Download failed. :(")

    print(f"Extracting {zip_path}!")
    z = zipfile.ZipFile(zip_path)
    z.extractall(output_path.parent)

    z.close()

    print("Deleting temp files...")
    print(f"Deleting {zip_path}...")
    os.remove(zip_path)
    print(f"Deleting {output_path}...")
    os.rmdir(output_path)

    _ = input("Success! Press [ENTER] to close.")


if __name__ == "__main__":
    main()
