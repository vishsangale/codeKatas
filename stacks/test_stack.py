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

    s.push(1)
    s.push(-2)
    s.push(-3)

    assert -3 == s.pop()
    assert -2 == s.pop()
    assert 1 == s.pop()

    with pytest.raises(IndexError):
        s.pop()

    s.push("a")
    s.push("b")
    s.push("d")

    assert 3 == len(s)

    assert "a<-b<-d" == str(s)

