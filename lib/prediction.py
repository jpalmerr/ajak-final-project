from keras.models import load_model
import sys
import numpy as np
sys.path.append('./helper_modules')
from constants import ITEMS

class Prediction():
    def __init__(self, drawing):
        self.drawing= drawing

    def predict(self):
        model = load_model("./models/first_model_training.h5")
        pred = ITEMS[np.argmax(model.predict(np.array([self.drawing])))]
        return pred
