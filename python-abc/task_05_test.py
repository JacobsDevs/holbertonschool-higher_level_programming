import pytest
from task_05_dragon import Dragon

class TestClass:
    def test_Dragon(self):
        draco = Dragon()

    def test_Dragon_fly(self, capfd):
        draco = Dragon()
        draco.fly()
        out, err = capfd.readouterr()
        assert out.split('\n')[-2] == "The creature flies!"

    def test_Dragon_swim(self, capfd):
        draco = Dragon()
        draco.swim()
        out, err = capfd.readouterr()
        assert out.split('\n')[-2] == "The creature swims!"

    def test_Dragon_roar(self, capfd):
        draco = Dragon()
        draco.roar()
        out, err = capfd.readouterr()
        assert out.split('\n')[-2] == "The dragon roars!"
