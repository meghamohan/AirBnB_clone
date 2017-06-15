#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """TestFileStorage"""
    def setUp(self):
        """Set up the instance"""
        self.filestorage = FileStorage()

    def testAttributes(self):
        """testing attributes of FileStorage"""
        self.assertFalse(hasattr(self.filestorage, "Holberton"))

    def testDocString(self):
        """tetsing for doc string"""
        exp = " returns __objects "
        self.assertEqual(exp, self.filestorage.all.__doc__)
        exp = " serializes __objects to the JSON"
        self.assertEqual(exp, self.filestorage.save.__doc__)
        exp = " deserializes the JSON file to __objects "
        self.assertEqual(exp, self.filestorage.reload.__doc__)
        exp = " contains methods to serialize and deserialize to objects "
        self.assertEqual(exp, self.filestorage.__doc__)

if "__main__" == __name__:
    unittest.main()
