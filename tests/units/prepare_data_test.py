import pytest
import sys
sys.path.append('../ajak-final-project/lib')
from prepare_data import *

def test_generate_labels_returns_array():
    assert generate_labels(2, 2) == [0, 0, 1, 1]

# print(set_limit([[0,1,2,3,4,5,6,7,8,9], [9, 8, 7, 6, 5, 4, 3, 2, 1]], 2))
