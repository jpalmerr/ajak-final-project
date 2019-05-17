import pytest
import sys
import numpy as np
from PIL import Image
sys.path.append('../ajak-final-project/lib')
from drawing import *

test_image = Image.open("tests/temp.png")

def test_instantiate_new_image():
  drawing = Drawing('test_data')
  assert type(drawing) is Drawing

def test_reshape_image_is_nparray():
    drawing = Drawing(test_image)
    drawing = drawing.reshape()
    assert type(drawing) is np.ndarray
