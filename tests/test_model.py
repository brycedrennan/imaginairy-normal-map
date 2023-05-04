from PIL import Image

from imaginairy_normal_map.model import create_normal_map_pil_img

from . import TESTS_DIR


def test_create_normal_map_pil_img():
    img = Image.open(f"{TESTS_DIR}/oval-office-large.jpg")
    create_normal_map_pil_img(img)
    # normal_img.save(f"{TESTS_DIR}/oval-office-large-normal.jpg")
    # normal_img.show()
