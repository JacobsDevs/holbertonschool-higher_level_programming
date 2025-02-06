import pytest
from task_04_flyingfish import FlyingFish, Fish, Bird

class TestClass:
    def test_FlyingFish(self):
        ff = FlyingFish()
        assert isinstance(ff, FlyingFish)

    def test_FlyingFish_fly(self, capfd):
        ff = FlyingFish()
        ff.fly()
        out, err = capfd.readouterr()
        assert out.split('\n')[-2] == "The flying fish is soaring!"

    def test_FlyingFish_swim(self, capfd):
        ff = FlyingFish()
        ff.swim()
        out, err = capfd.readouterr()
        assert out.split('\n')[-2] == "The flying fish is swimming!"

    def test_FlyingFish_habitat(self, capfd):
        ff = FlyingFish()
        ff.habitat()
        out, err = capfd.readouterr()
        assert out.split('\n')[-2] == "The flying fish lives both in water and the sky!"

    def test_FlyingFish_mro(self):
        assert FlyingFish.mro() == [FlyingFish, Fish, Bird, object]

