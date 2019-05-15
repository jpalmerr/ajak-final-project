import numpy as np
from keras.models import load_model
from random import randint
from prepare_data import normalize, load
from train import predict

model = load_model("./models/first_model_training.h5")

# def predict():
    # SHAPES = {0: "Circle", 1: "Square", 2: "Triangle"}
    # "selects a random test case and shows the object, the prediction and the expected result"
    # shapes = load("data/", files, True)
    # shapes = set_limit(shapes, 1)
    # shapes = list(map(normalize, shapes))
    # val = model.predict(np.array(shapes))
    # pred = SHAPES[np.argmax(val)]
    # print("Predicted: ", pred)
    # print("Actual: ", actual)

    # n = randint(0, len(x_test))
    # pred = SHAPES[np.argmax(model.predict(np.array([x_test[n]])))]
    # actual = SHAPES[y_test[n]]
    # print("Actual:"), actual
    # print("Predicted:"), pred


# print("Making a prediction")
# predict()
