import numpy as np
from PIL import Image
from prepare_data import normalize

class Drawing():
    def __init__(self, image):
        self.image = image

    def reshape(self):
        img = (self.image).resize((28,28))
        np_img = np.array(img)
        np_img = normalize(np_img)
        return np_img
