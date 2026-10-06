import pytest
from bank import value

def test_bank_witout_Hello():

    assert value("Hello") == "$0"
    assert value("hello") == "$0"

def test_bank_witout_H():

    assert value("Hola") == "$20"
    assert value("hola") == "$20"

def test_bank_witout():

    assert value("jeje") == "$100"