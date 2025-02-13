import unittest
from task_01_pickle import CustomObject

class TestClass(unittest.TestCase):
    def test_CustomObject_instantiation(self):
        c = CustomObject("John", 7, True)
        self.assertEqual(c.name, "John")
        self.assertEqual(c.age, 7)
        self.assertEqual(c.is_student, True)

    def test_CustomObject_serialize_deserialize(self):
        c = CustomObject("John", 7, True)
        c.serialize("test_object.json")
        b = CustomObject.deserialize("test_object.json")
        self.assertEqual(b.__dict__, c.__dict__)

    def test_deserialize_nonexistant_file(self):
        b = CustomObject.deserialize("no_file.txt")
        self.assertEqual(b, None)

    def test_zcorrupt_file(self):
        b = CustomObject.deserialize("corrupt_file.txt")
        self.assertEqual(b, None)
