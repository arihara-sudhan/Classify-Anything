import os
import glob

def count_files_in_subfolders(directory):
    total_files = 0
    for subfolder in os.listdir(directory):
        subfolder_path = os.path.join(directory, subfolder)
        if os.path.isdir(subfolder_path):
            files = glob.glob(os.path.join(subfolder_path, '*'))
            total_files += len(files)
    return total_files

train_dir = '../dataset/train'
test_dir = '../dataset/test'

train_files_count = count_files_in_subfolders(train_dir)
test_files_count = count_files_in_subfolders(test_dir)

print(f"Total files in train subfolders: {train_files_count}")
print(f"Total files in test subfolders: {test_files_count}")