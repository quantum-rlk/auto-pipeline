
import pytest
from decoy import echo

MSG1='calling pipeline job .....'
MSG2='..............'

def test_echo():
    res = echo(MSG1)
    assert res == 1

