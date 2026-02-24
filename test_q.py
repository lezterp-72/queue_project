from q import *

def test_empty():
    ls = Queue()
    assert ls.empty()
    ls.add("Hello")
    assert not ls.empty()

def test_add():
    ls = Queue()
    ls.add(1)
    assert ls.head.data
    ls.add(2)
    assert ls.head.next.data
    ls.add(3)
    assert ls.head.next.next.data

def test_pop():
    ls = Queue()
    ls.add(1)
    ls.add(2)
    ls.add(3)
    ls.pop_left()
    assert ls.head.data == 2
    ls.pop_left()
    assert ls.head.data == 3


