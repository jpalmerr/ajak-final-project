from keras.models import load_model
import sys
import numpy as np
sys.path.append('./helper_modules')
from constants import SHAPES

class Prediction():
    def __init__(self, image):
        self.image = image

    def predict(self):
        model = load_model("./models/first_model_training.h5")
        print('we have loaded the model')
        print(np.array(self.image))
        pred = SHAPES[np.argmax(model.predict(np.array(self.image)))]
        print('this is our prediction')
        print(pred)
        print('this is the end of the prediction')
        return 1
