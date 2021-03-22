import pytest

from stack import Stack

def test_basic_operations():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()

    with pytest.raises(IndexError):
        s.peak()

    s.push(100)

    assert 100 == s.peak()

    assert 1 == len(s)

    assert 100 == s.pop()

    assert 0 == len(s)


