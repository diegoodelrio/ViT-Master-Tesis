import os
import pandas as pd
import requests
import time
import random
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# --- CONFIGURATION ---
# This path works on both Spanish (Descargas) and English Macs
TARGET_DIR = os.path.expanduser('~/Downloads/Images_Data_Thesis')
NUM_THREADS = 2  # Keep this LOW to avoid HTTP 429 (Too Many Requests)
LANDMARKS_TO_DOWNLOAD = [
    47378, 141899,
    156556, 168098, 165596, 
    10419, 190822, 55350, 
    161902, 139706, 113224,
    113260, 187779, 9070,
    136093, 20120, 176018,
    164773, 40088
]

def download_image(row):
    img_id, url, landmark_id = row
    
    # Create the subfolder path
    folder = os.path.join(TARGET_DIR, str(landmark_id))
    os.makedirs(folder, exist_ok=True)
    
    file_path = os.path.join(folder, f"{img_id}.jpg")
    
    # Skip if already downloaded
    if os.path.exists(file_path):
        return
    
    # Identify yourself to the server to look less like a generic bot
    headers = {
        'User-Agent': 'ThesisResearchBot/1.0 (Contact: yourname@university.edu) Research on Landmark Attention',
        'Accept-Language': 'en-US,en;q=0.5'
    }
    
    try:
        # 1. Be polite: Random sleep so we don't hit the server too hard
        time.sleep(random.uniform(0.3, 0.8))
        
        r = requests.get(url, headers=headers, timeout=15, stream=True)
        
        if r.status_code == 200:
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        elif r.status_code == 429:
            # If the server tells us to slow down, we listen!
            print(f"\n[Warning] Throttled (429). Waiting 30 seconds...")
            time.sleep(30)
    except Exception:
        # Silent fail for individual images to keep the progress bar moving
        pass

if __name__ == '__main__':
    print("Step 1: Loading metadata...")
    # Update this path if your train.csv is elsewhere
    if not os.path.exists('Data/train.csv'):
        print("Error: Could not find Data/train.csv. Please check the path!")
    else:
        df = pd.read_csv('Data/train.csv')
        
        print("Step 2: Filtering landmarks...")
        subset = df[df['landmark_id'].isin(LANDMARKS_TO_DOWNLOAD)]
        data_list = list(subset.itertuples(index=False, name=None))
        
        print(f"Target Folder: {TARGET_DIR}")
        print(f"Attempting to download {len(data_list)} images...")
        
        # Step 3: Start the controlled download
        with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
            list(tqdm(executor.map(download_image, data_list), total=len(data_list)))

        print("\nDownload process complete. Check your Downloads/Images_Data_Thesis folder!")
