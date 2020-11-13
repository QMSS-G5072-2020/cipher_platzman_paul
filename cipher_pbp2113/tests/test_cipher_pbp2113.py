from cipher_pbp2113 import __version__
from cipher_pbp2113 import cipher_pbp2113
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_cipher_negative_shift():
    actual = cipher_pbp2113.cipher("Johnny",-5)
    expected = 'Ejciit'
    assert actual == expected