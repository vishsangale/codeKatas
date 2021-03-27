import pytest

from katas.queues.queue import Queue
from katas.queues.queue_using_two_stacks import QueueFromStacks


def test_basic_operations():
    q = Queue()
    with pytest.raises(IndexError):
        q.peek()

    with pytest.raises(IndexError):
        q.dequeue()

    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(5)

    assert 3 == len(q)

    assert 2 == q.peek()

    assert 3 == len(q)

    assert "2<-4<-5" == str(q)

    assert 2 == q.dequeue()

    assert 2 == len(q)

    assert "4<-5" == str(q)

    q.dequeue()
    q.dequeue()

    assert 0 == len(q)

    q.enqueue(4)

    assert 4 == q.peek()


def test_queue_from_stacks():
    q = QueueFromStacks()
    with pytest.raises(IndexError):
        q.peek()

    with pytest.raises(IndexError):
        q.dequeue()

    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(5)

    assert 3 == len(q)

    assert 2 == q.peek()

    assert 3 == len(q)

    assert 2 == q.dequeue()

    assert 2 == len(q)

    q.dequeue()
    q.dequeue()

    assert 0 == len(q)

    q.enqueue(4)

    assert 4 == q.peek()
