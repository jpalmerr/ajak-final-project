import pytest
import sys
sys.path.append('./lib')
from prediction import *

def test_create_prediction():
    prediction = Prediction("Image")
    assert type(prediction) is Prediction
