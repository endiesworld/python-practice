from pathlib import Path

# For local test only, Directory to save uploaded images
UPLOAD_DIR = Path.cwd() / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

async def fn_upload_meal():

    image_path = UPLOAD_DIR / meal.filename
    
    try:
        # Save the file to the uploads directory
        with image_path.open("wb") as buffer:
            buffer.write(await meal.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail="File upload failed")
    
    return {"filename": meal.filename, "file_path": str(image_path), "label": str(label)}