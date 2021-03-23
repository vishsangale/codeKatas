import pytest

from queue import Queue


def test_basic_operations():
    q = Queue()
    with pytest.raises(IndexError):
        q.peek()

    with pytest.raises(IndexError):
        q.poll()

    q.add(2)
    q.add(4)
    q.add(5)

    assert 3 == len(q)

    assert 2 == q.peek()

    assert 3 == len(q)

    assert "2<-4<-5" == str(q)

    assert 2 == q.poll()

    assert 2 == len(q)

    assert "4<-5" == str(q)

    q.poll()
    q.poll()

    assert 0 == len(q)

    q.add(4)

    assert 4 == q.peek()
