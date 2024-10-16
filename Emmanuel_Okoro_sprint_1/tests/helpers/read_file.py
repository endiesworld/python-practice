from pathlib import Path



# For local test only, Directory to save uploaded images
IMAGE_PATH = Path.cwd()/'tests'/'helpers' /'meal.jpg'


# Function to read the image
def read_image(image_path):
    
    try:
        # Read the image as binary
        with open(image_path, 'rb') as f:
            image_bytes = f.read()
        return  image_bytes
    except FileNotFoundError:
        raise FileNotFoundError("Image not found at the specified path.")
    

