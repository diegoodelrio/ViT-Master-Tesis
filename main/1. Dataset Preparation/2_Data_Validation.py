import os
from PIL import Image #Package used for verifying pixel data
from tqdm import tqdm

BASE_PATH = os.path.expanduser('~/Desktop/Master Thesis/Data/Images_Data_Thesis')

def clean_sweep():
    print(f"Starting Clean Sweep in: {BASE_PATH}")
    #Validate that the path exists

    if not os.path.exists(BASE_PATH):
        print("Error: The path does not exists.")
        return

    stats = {"zero_byte": 0, "Corrupt": 0, "Valid": 0}

    #Loop through each of the landmark ID folders
    for root, _, files in os.walk(BASE_PATH):
        for file in tqdm(files, desc=f"Scanning {os.path.basename(root)}"):
            file_path = os.path.join(root, file)

            #Step 1: Zero-Byte Check
            if os.path.getsize(file_path) == 0:
                os.remove(file_path)
                stats["zero_byte"] += 1
                continue

            #Ste 2: Integrity & Pixel Decoding Check
            try:
                with Image.open(file_path) as img:
                    img.verify() #Structural check
                with Image.open(file_path) as img:
                    img.load()
                stats["Valid"] += 1
            except Exception:
                os.remove(file_path)
                stats["Corrupt"] += 1

    print("\n--- Phase 1.1 Report ---")
    print(f"Valid Images: {stats['Valid']}")
    print(f"Empty Files Deleted: {stats['zero_byte']}")
    print(f"Corrupt Files Deleted: {stats['Corrupt']}")

if __name__ == "__main__":
    clean_sweep()

     
