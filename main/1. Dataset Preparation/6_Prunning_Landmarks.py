import os
import shutil

BASE_PATH = os.path.expanduser('~/Desktop/Master Thesis/Data/Split_Dataset')
ARCHIVE_PATH = os.path.expanduser('~/Desktop/Master Thesis/Data/Filtered_Out_Small_Classes')
THRESHOLD = 100

def prune_dataset():
    train_path = os.path.join(BASE_PATH, 'train')

    if not os.path.exists(train_path):
        print(f"Error: No se encontro la carpeta de entrenamiento en {train_path}")
        return
    
    lids = [d for d in os.listdir(train_path) if os.path.isdir(os.path.join(train_path, d)) and not d.startswith('.')]

    to_remove = []

    print(f"Analizando {len(lids)} categorias...")

    for lid in lids:
        lid_path = os.path.join(train_path, lid)

        num_images = len([f for f in os.listdir(lid_path) if not f.startswith('.')])

        if num_images < THRESHOLD:
            to_remove.append((lid, num_images))

    if not to_remove:
        print("Todas las categorias cumplen con el umbral de 100 imagenes")
        return
    
    print(f"Se encontraron {len(to_remove)} categorias pro debajo del umbral.")

    for lid, count in to_remove:
        print(f"Archivando ID: {lid} ({count} imagenes)")

        for split in ['train', 'val', 'test']:
            src = os.path.join(BASE_PATH, split, lid)
            dst = os.path.join(ARCHIVE_PATH,split,lid)

            if os.path.exists(src):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.move(src, dst)

    print(f"\n Limpieza completada. Las categorias eliminadas estan en {ARCHIVE_PATH}")

if __name__=="__main__":
    prune_dataset()
