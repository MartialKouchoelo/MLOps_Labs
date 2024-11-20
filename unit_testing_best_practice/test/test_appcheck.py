import sys
import pytest
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from appcheck import *

#@pytest.mark.parametrize("username, password, email", [["Mugen", "Bl@ckmamba24", "spero.tossogbe@epitech.eu"]])
#def test_return_value(username, password, email):
#    assert func(username, password, email) == True

def test_answer():
    assert func("Mugen", "Bl@ckmamba24", "spero.tossogbe@epitech.eu") == True