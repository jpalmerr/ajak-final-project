import pytest
import sys
import numpy as np
sys.path.append('./lib')
from prepare_data import *

files = ["test.npy"]

def test_load_returns_list_of_numpy_array():
    'Load method takes file path, array of files and reshaped boolean and returns list'
    assert type(load("tests/units/", files, True)) is list

def test_normalize_returns_np_ndarray():
    'Normalize method takes loaded data and returns a np array'
    assert type(normalize([1,2,3,4,5])) is np.ndarray

def test_normalize_returns_value_between_1_and_minus_1():
    'Normalize method takes loaded data and items in returned array are normalized'
    assert -1 <= normalize([1])[0] <= 1

def test_set_limit_generates_single_limited_list():
    'Set limit method takes array of arrays and number n, returns single array with n items from each array'
    assert set_limit([[0,1,2,3], [9,8,7,6]], 2) == [0,1,9,8]

def test_set_limit_generates_empty_array():
    'Set limit edge case to check can return empty array'
    assert set_limit([[],[]], 2) == []

def test_generate_labels_returns_array():
    'Generate label method takes no. of classes and no. of samples and returns array from 0 to no. of classes multiplied by no. of samples'
    assert generate_labels(2, 2) == [0, 0, 1, 1]

def test_generate_labels_returns_empty_array():
    'Generate label edge case to check can return empty array'
    assert generate_labels(0, 0) == []
