import os
import random
import shutil
from tqdm import tqdm

#SOURCE: Where the cleaned ID foledrs are
SOURCE_PATH = os.path.expanduser('~/Desktop/Master Thesis/Data/Images_Data_Thesis')

#DESTINATION: Destination folder for the organised 80/10/10 files
FINAL_PATH = os.path.expanduser('~/Desktop/Master Thesis/Data/Split_Dataset')

def execute_split(train_perc = 0.8, val_perc = 0.1):
    
    #1. Setup the basice folders
    splits = ['train', 'val', 'test']
    for s in splits:
        os.makedirs(os.path.join(FINAL_PATH, s), exist_ok=True)
    
    #2. Get all landmark ID folders
    landmark_ids = [d for d in os.listdir(SOURCE_PATH) if os.path.isdir(os.path.join(SOURCE_PATH, d))]
    print(f"FOund {len(landmark_ids)} landmark categories. Starting split...")

    for landmark in tqdm(landmark_ids, desc="Processing Landmarks"):
        landamrk_source = os.path.join(SOURCE_PATH, landmark)
        images = [f for f in os.listdir(landamrk_source) if not f.startswith('.')]

        #Shuffle images randombly
        random.seed(42)
        random.shuffle(images)

        #Calculate Index
        train_end = int(len(images) * train_perc)
        val_end = train_end + int(len(images) * val_perc)

        image_splits = {
            'train': images[:train_end],
            'val': images[train_end:val_end],
            'test': images[val_end:]
        }

        for split_name, split_files in image_splits.items():
            split_folder = os.path.join(FINAL_PATH, split_name, landmark)
            os.makedirs(split_folder, exist_ok=True)

            for img in tqdm(split_files, desc="Processing Image copying"):
                shutil.copy2(os.path.join(landamrk_source, img), os.path.join(split_folder, img))
    
    print(f"\n Structural Split Completed! Files are now in {FINAL_PATH}")

if __name__ == "__main__":
    execute_split()
