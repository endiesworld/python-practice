from helpers.read_file import IMAGE_PATH, read_image
from helpers.path_generator import generate_random_path

from upload_meal import fn_upload_meal_label

FUNCTION_TO_TEST = fn_upload_meal_label
BASE_DIR = "uploads"
BASE_EXTENSION = "jpg"

class TestUploadMeal:

    def test_fn_upload_meal_true(self):
        image = read_image(IMAGE_PATH)
        base_dir, file_name = generate_random_path(BASE_DIR, BASE_EXTENSION)
        result = FUNCTION_TO_TEST(image,base_dir, file_name)
        assert result != None
        
        
    def test_fn_upload_meal_path(self):
        image = read_image(IMAGE_PATH)
        base_dir, file_name = generate_random_path(BASE_DIR, BASE_EXTENSION)
        result = FUNCTION_TO_TEST(image,base_dir, file_name)
        assert result["message"] == "Upload successful!"
        assert result["path"] == str(base_dir / f"{file_name}")