import pathlib
import pytest
from mymath.calculator import add


# Simple test
# ----------------------------------------------------
def test_add():
    assert add(1, 2) == 3


# Test organized in class
# ------------------------------------------------------------------------------
class TestCalculator:

    def test_add(self):
        assert add(1, 2) == 3


# Fixtures
# ------------------------------------------------------------------------------
@pytest.fixture(scope="function")
def read_data_from_files():
    my_path = pathlib.Path(__file__).resolve()
    with open(str(my_path.parents[1]) + "/test/data/numbers.txt") as fp:
        numbers = [int(line.rstrip()) for line in fp]

    return numbers


def test_filesum(read_data_from_files):
    num = read_data_from_files
    assert add(num[0], num[1]) == num[2]
