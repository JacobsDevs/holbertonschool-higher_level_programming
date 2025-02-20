#!/usr/bin/python3

from task_03_http_server import *
import requests
import unittest
import threading
import time

class TestClass(unittest.TestCase):

    thread = threading.Thread(target=start_server)

    @classmethod
    def setUpClass(cls) -> None:
        cls.thread.start()

    def test_get_request(self):
        time.sleep(0.00001)
        data = requests.get('http://localhost:8000')
        self.assertEqual(data.content, b'Hello, this is a simple API!')

    def test_get_data(self):
        time.sleep(0.00001)
        data = requests.get('http://localhost:8000/data')
        self.assertEqual(data.headers['Content-Type'], 'application/json')
        self.assertEqual(data.content, b'{"name": "John", "age": 30, "city": "New York"}')

    def test_get_status(self):
        time.sleep(0.00001)
        data = requests.get('http://localhost:8000/status')
        self.assertEqual(data.content, b'OK')

    def test_get_404(self):
        time.sleep(0.00001)
        data = requests.get('http://localhost:8000/hackthesite')
        self.assertEqual(data.status_code, 404)
        self.assertEqual(data.content, b'/hackthesite Page Not Found')
