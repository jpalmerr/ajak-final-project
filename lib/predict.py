import sys
sys.path.append('./helper_modules')
from keras.models import load_model
from random import randint
from constants import *
from load_data import *

def predict():
    model = load_model("./models/first_model_training.h5")
    "selects a random test case and shows the object, the prediction and the expected result"
    n = randint(0, len(x_test))
    pred = SHAPES[np.argmax(model.predict(np.array([x_test[n]])))]
    actual = SHAPES[y_test[n]]
    print("Actual:", actual)
    print("Predicted:", pred)

print("Making a prediction")
predict()
