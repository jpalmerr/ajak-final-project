import numpy as np
from PIL import Image

class Drawing():
    def __init__(self, image):
        self.image = image

    def reshape(self):
        img = (self.image).resize((28,28))
        np_img = np.array(img)
        # need to normalize
        return(np_img)
