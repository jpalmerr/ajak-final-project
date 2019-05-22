import pytest
import sys
import keras
sys.path.append('./lib')
from conv import *

def test_conv_returns_keras_sequential_model():
    assert isinstance(conv(3, (28, 28, 1)), keras.engine.sequential.Sequential)
