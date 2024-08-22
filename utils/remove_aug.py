import os

def remove_augmented_images(directory, prefix='aug_'):
    for subfolder in os.listdir(directory):
        subfolder_path = os.path.join(directory, subfolder)
        if os.path.isdir(subfolder_path):
            for filename in os.listdir(subfolder_path):
                if filename.lower().startswith(prefix.lower()):
                    file_path = os.path.join(subfolder_path, filename)
                    os.remove(file_path)
                    print(f"Removed: {file_path}")

train_dir = '../dataset/train'
test_dir = '../dataset/test'
remove_augmented_images(train_dir, 'augmented_')
remove_augmented_images(test_dir, 'augmented_')
