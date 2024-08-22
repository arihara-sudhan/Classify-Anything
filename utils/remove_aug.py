import os

def remove_aug_files(directory):
    for subfolder in os.listdir(directory):
        subfolder_path = os.path.join(directory, subfolder)
        if os.path.isdir(subfolder_path):
            for filename in os.listdir(subfolder_path):
                if filename.lower().startswith('aug'):
                    file_path = os.path.join(subfolder_path, filename)
                    os.remove(file_path)
                    print(f"Removed: {file_path}")

train_dir = '../dataset/train'
test_dir = '../dataset/test'
remove_aug_files(train_dir)
remove_aug_files(test_dir)