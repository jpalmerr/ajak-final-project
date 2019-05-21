import pytest
import sys
sys.path.append('./lib')
from prediction import *
from drawing import *

test_image = Image.open("tests/temp.png")
# yet to mock the Image class

def test_create_prediction():
    prediction = Prediction("Image")
    assert type(prediction) is Prediction

def test_can_make_prediction():
    drawing = Drawing(test_image)
    drawing = drawing.reshape()
    prediction = Prediction(drawing)
    assert prediction.predict() == 'Triangle'
