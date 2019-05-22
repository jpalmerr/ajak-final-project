import pytest
import sys
sys.path.append('./lib')
from prediction import *
from drawing import *

test_image = Image.open("tests/temp.png")
# yet to mock the Image class

def test_can_make_prediction():
    'Prediction takes a drawing object and predict method returns a prediction as string'
    drawing = Drawing(test_image)
    drawing = drawing.reshape()
    prediction = Prediction(drawing)
    assert prediction.predict() == 'Crown'
