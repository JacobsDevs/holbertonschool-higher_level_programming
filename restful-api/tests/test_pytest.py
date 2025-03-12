import requests
import threading
import time
import pytest

class TestClass:
    def test_one(self):
        x = "this"
        assert "s" in x

class TestClassTwo:
    def test_two(self):
        x = "this"
        assert "s" in x

class TestClassThree:
    def test_two(self):
        x = "quit"
        assert "w" in x
