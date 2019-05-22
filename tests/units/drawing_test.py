import pytest
import sys
import numpy as np
from PIL import Image
sys.path.append('./lib')
from drawing import *

test_image = Image.open("tests/temp.png")

def test_reshape_image_returns_nparray():
    'Drawing takes a png file and when calling reshape, returns np array'
    drawing = Drawing(test_image)
    drawing = drawing.reshape()
    assert type(drawing) is np.ndarray

def test_reshape_image_is_normalized():
    'Drawing takes a png file and when calling reshape, items in returned np array are normalized'
    drawing = Drawing(test_image)
    drawing = drawing.reshape()
    assert -1 <= drawing.all() <= 1
