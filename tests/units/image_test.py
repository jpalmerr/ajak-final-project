import pytest
import sys
sys.path.append('../ajak-final-project/lib')
from image import *

def test_instantiate_new_image():
  img = Image('test_data')
  assert type(img) is Image