import cv2
import numpy as np

def load_image(img_file):
    img = cv2.imdecode(np.frombuffer(img_file.read(), np.uint8), 1)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def resize_image(img, size=(256, 256)):
    return cv2.resize(img, size)

def normalize_rgb(img):
    return img / 255.0

