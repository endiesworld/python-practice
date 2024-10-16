from pathlib import Path
import uuid

# Function to generate a random path and filename
def generate_random_path(base_dir, extension="jpg"):
    base_dir = Path(base_dir)
    
    # Ensure base directory exists
    base_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate a unique filename
    file_name = f"{uuid.uuid4()}.{extension}"
    
    # Create the full path
    return  base_dir, file_name
