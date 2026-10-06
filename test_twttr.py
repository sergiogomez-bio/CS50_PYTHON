import pytest 
from twttr import shorten 

def test_shorten():
    ...
    assert shorten("Sergio Mateo")=="Srg Mt"
    assert shorten("Cs50")=="Cs50"