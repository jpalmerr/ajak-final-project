from random import randint
import sys
from keras.models import load_model
sys.path.append('./helper_modules')
from constants import *
from load_data import *

def predict_on_test_data_in_command_line():
    model = load_model("./models/cameras_rabbits_crowns_model.h5")
    # selects a random test case and shows the object, the prediction and the expected result
    n = randint(0, len(x_test))
    pred = ITEMS[np.argmax(model.predict(np.array([x_test[n]])))]
    actual = ITEMS[y_test[n]]
    print("Making a prediction")
    print("Actual:", actual)
    print("Predicted:", pred)

predict_on_test_data_in_command_line()
