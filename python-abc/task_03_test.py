import pytest
from task_03_countediterator import CountedIterator

class TestClass:
    def test_initializes(self):
        ci = CountedIterator([1, 2, 3])
        assert isinstance(ci, CountedIterator)

    def test_next(self):
        with pytest.raises(StopIteration):
            ci = CountedIterator([1, 2, 3])
            next(ci)
            next(ci)
            next(ci)
            next(ci)

    def test_counter(self, capfd):
        ci = CountedIterator([1, 2, 3])
        next(ci)
        print("Counter: {}".format(ci.counter))
        next(ci)
        print("Counter: {}".format(ci.counter))
        next(ci)
        print("Counter: {}".format(ci.counter))
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "Counter: 3"
