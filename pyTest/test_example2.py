import pytest

from pyTest.test_example1 import hi, bye, how_are_you


@pytest.fixture
def akd():
    return {"name" : "AKD"}


def test_hello(akd):
    assert hi(akd) == "Hi, AKD"

def test_bye(akd):
    assert bye(akd) == "Bye, AKD"

def test_how_are_you(akd):
    assert how_are_you(akd) == "How are you AKD ?"