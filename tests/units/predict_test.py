import pytest
import sys
sys.path.append('./lib')
from predict import *

def test_predict_on_test_data_to_stdout(capsys):
    predict_on_test_data()
    captured = capsys.readouterr()
    assert 'Predicted' in captured.out
    assert 'Actual' in captured.out
