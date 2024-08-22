import os
import random
from PIL import Image, ImageFilter, ImageDraw

def create_random_circle_mask(size, circle_area_percentage=0.6):
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    
    radius = int((circle_area_percentage * size[0] * size[1] / (3.14 * 4))**0.5)
    x, y = random.randint(radius, size[0] - radius), random.randint(radius, size[1] - radius)
    
    draw.ellipse([(x - radius, y - radius), (x + radius, y + radius)], fill=255)
    return mask

def augment_image(image):
    augmented_images = []

    image = image.resize((224, 224))

    # Rotation
    for angle in [90, 180, 270]:
        rotated_image = image.rotate(angle)
        augmented_images.append(rotated_image)

    # Blur
    blurred_image = image.filter(ImageFilter.BLUR)
    augmented_images.append(blurred_image)

    # Masking
    mask = create_random_circle_mask(image.size)
    masked_image = Image.composite(image, Image.new('RGB', image.size, (0, 0, 0)), mask)
    augmented_images.append(masked_image)

    return augmented_images

def augment_directory(directory, target_count):
    for subfolder in os.listdir(directory):
        subfolder_path = os.path.join(directory, subfolder)
        if os.path.isdir(subfolder_path):
            images = [f for f in os.listdir(subfolder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            current_count = len(images)
            print(f"Processing folder: {subfolder_path} with {current_count} images")

            if current_count < target_count:
                original_images = [Image.open(os.path.join(subfolder_path, img)) for img in images]
                augmented_images = []
                for img in original_images:
                    augmented_images.extend(augment_image(img))
                
                # Calculate how many augmented images are needed
                augmented_needed = target_count - current_count
                print(f"Need {augmented_needed} more augmented images")

                # Save augmented images
                saved_count = 0
                for i, img in enumerate(augmented_images):
                    if saved_count >= augmented_needed:
                        break
                    filename = f'aug_{i}.png'
                    img.save(os.path.join(subfolder_path, filename))
                    saved_count += 1
                
                print(f"Saved {saved_count} augmented images")

train_dir = '../dataset/train'
test_dir = '../dataset/test'
augment_directory(train_dir, 50)
augment_directory(test_dir, 50)
