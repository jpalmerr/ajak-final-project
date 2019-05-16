import pytest
import sys
sys.path.append('../ajak-final-project/lib')
from prepare_data import *

def test_set_limit_generates_single_limited_list():
    assert set_limit([[0,1,2,3], [9,8,7,6]], 2) == [0,1,9,8]

def test_set_limit_generates_empty_array():
    assert set_limit([[],[]], 2) == []

def test_generate_labels_returns_array():
    assert generate_labels(2, 2) == [0, 0, 1, 1]

def test_generate_labels_returns_empty_array():
    assert generate_labels(0, 0) == []
