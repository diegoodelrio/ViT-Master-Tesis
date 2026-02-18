import os
from PIL import Image
from tqdm import tqdm

# Targeted path
BASE_PATH = os.path.expanduser('~/Desktop/Master Thesis/Data/Split_Dataset')
SPLITS = ['train', 'val', 'test']
SIZE = (224, 224)

def targeted_standardization():
    print(f"Starting targeted resize at: {BASE_PATH}")
    total_processed = 0

    for split in SPLITS:
        split_path = os.path.join(BASE_PATH, split)
        
        if not os.path.exists(split_path):
            print(f"Warning: Split folder not found: {split_path}")
            continue

        # Get the Landmark ID folders inside (e.g., '47378')
        landmark_ids = [d for d in os.listdir(split_path) if not d.startswith('.')]
        
        print(f"\nProcessing {split.upper()} split...")

        for lid in landmark_ids:
            lid_path = os.path.join(split_path, lid)
            if not os.path.isdir(lid_path):
                continue
                
            # Get the actual image files
            files = [f for f in os.listdir(lid_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            
            for file in tqdm(files, desc=f"ID: {lid}", leave=False):
                file_path = os.path.join(lid_path, file)
                
                try:
                    with Image.open(file_path).convert('RGB') as img:
                        # Resizing with aspect ratio preservation
                        img.thumbnail(SIZE, Image.Resampling.LANCZOS)
                        
                        # Create black background canvas
                        canvas = Image.new("RGB", SIZE, (0, 0, 0))
                        offset = ((SIZE[0] - img.size[0]) // 2, (SIZE[1] - img.size[1]) // 2)
                        canvas.paste(img, offset)
                        
                        # Save it back
                        canvas.save(file_path, "JPEG", quality=90)
                        total_processed += 1
                except Exception as e:
                    print(f"Error processing {file}: {e}")

    print(f"\nSUCCESS! Total standardized images: {total_processed}")

if __name__ == "__main__":
    targeted_standardization()