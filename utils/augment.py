import os
import random
from PIL import Image, ImageFilter

def augment_image(image):
    # Resize the image to 224x224
    image = image.resize((224, 224))
    
    # Apply Gaussian Blur
    if random.random() > 0.5:
        image = image.filter(ImageFilter.GaussianBlur(radius=4))
    
    # Apply Random Rotation
    if random.random() > 0.5:
        angle = random.randint(0, 360)
        image = image.rotate(angle, expand=True)
        # Resize again to ensure the image is 224x224
        image = image.resize((224, 224))
    
    return image

def augment_directory(directory, target_count):
    for subfolder in os.listdir(directory):
        subfolder_path = os.path.join(directory, subfolder)
        if os.path.isdir(subfolder_path):
            images = [f for f in os.listdir(subfolder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
            num_images = len(images)
            
            while num_images < target_count:
                original_image_path = os.path.join(subfolder_path, random.choice(images))
                original_image = Image.open(original_image_path)
                augmented_image = augment_image(original_image)
                
                # Ensure unique image names
                augmented_image_name = f"augmented_{num_images}.png"
                while os.path.exists(os.path.join(subfolder_path, augmented_image_name)):
                    num_images += 1
                    augmented_image_name = f"augmented_{num_images}.png"
                
                augmented_image.save(os.path.join(subfolder_path, augmented_image_name))
                num_images += 1

train_dir = '../dataset/train'
test_dir = '../dataset/test'
augment_directory(train_dir, 50)
augment_directory(test_dir, 50)
