from pathlib import Path

# For local test only, Directory to save uploaded images
UPLOAD_DIR = Path.cwd() / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

def fn_upload_meal_label(meal, save_dir, label):

    save_dir = Path(save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)
    
    save_path = save_dir / label
    
    try:
        # Save the file to the uploads directory
        with open(save_path, 'wb') as f:
            f.write(meal)
    
        return {"message": "Upload successful!" , "path": str(save_path)}
    
    except FileNotFoundError:
        raise FileNotFoundError("Image not found at the specified path.")
    