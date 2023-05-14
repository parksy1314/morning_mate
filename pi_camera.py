import time
from PIL import Image
import subprocess

photo_path = "/mnt/gdrive/mirror_photo.jpg"
subprocess.run(["libcamera-still", "-o",photo_path])
time.sleep(2)


