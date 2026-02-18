import os
import matplotlib.pyplot as plt
from PIL import Image
import random

BASE_PATH = os.path.expanduser('~/Desktop/Master Thesis/Data/Split_Dataset')

def perform_eda():
    
    splits = ['train', 'val', 'test']
    stats = {}

    print("Calculating Class Distribution....")
    for split in splits:
        split_path = os.path.join(BASE_PATH, split)
        stats[split] = {}

        #Get Landmark IDs
        lids = [d for d in os.listdir(split_path) if not d.startswith('.')]
        for lid in lids:
            count = len(os.listdir(os.path.join(split_path, lid)))
            stats[split][lid] = count
        
    # --- Print Stats Table ---
    print(f"{'Landmark ID':<15} | {'Train':<8} | {'Val':<8} | {'Test':<8}")
    print("-" * 45)
    for lid in stats['train'].keys():
        tr = stats['train'].get(lid, 0)
        va = stats['val'].get(lid, 0)
        te = stats['test'].get(lid, 0)
        print(f"{lid:<15} | {tr:<8} | {va:<8} | {te:<8}")

    # --- Visual Verification ---
    print("\nDisplaying Random Sample Grid...")
    fig, axes = plt.subplots(3, 5, figsize=(15, 10))
    fig.suptitle("Resized & Padded Landmark Samples (224x224)", fontsize=16)

    # Pick random images from the Train set
    all_train_folders = [os.path.join(BASE_PATH, 'train', d) for d in os.listdir(os.path.join(BASE_PATH, 'train'))]
    
    for i in range(15):
        random_folder = random.choice(all_train_folders)
        random_img_name = random.choice(os.listdir(random_folder))
        img_path = os.path.join(random_folder, random_img_name)
        
        img = Image.open(img_path)
        ax = axes[i//5, i%5]
        ax.imshow(img)
        ax.set_title(os.path.basename(random_folder))
        ax.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    perform_eda()   