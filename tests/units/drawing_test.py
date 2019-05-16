import pytest
import sys
from PIL import Image
sys.path.append('../ajak-final-project/lib')
from drawing import *

test_image = Image.open("tests/temp.png")

def test_instantiate_new_image():
  drawing = Drawing('test_data')
  assert type(drawing) is Drawing

def test_resize_image():
  drawing = Drawing(test_image)
  drawing = drawing.resize()
  assert drawing.size == (28,28)

