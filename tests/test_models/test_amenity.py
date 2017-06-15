#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class AmenityTest(unittest.TestCase):
    """ unittest for BaseModel class"""
    def setUp(self):
        """ create a new instance """
        self.cls = Amenity()

    def testType(self):
        """test type"""
        self.assertEqual(self.cls.__class__.__name__, "Amenity")

    def testAttributes(self):
        """test all attributes"""
        self.assertTrue(hasattr(self.cls, "id"))
        self.assertTrue(hasattr(self.cls, "created_at"))
        self.assertFalse(hasattr(self.cls, "updated_at"))
        self.assertFalse(hasattr(self.cls, "Holberton"))
        self.cls.school = "Holberton"
        self.cls.phno = 408505
        self.assertTrue(hasattr(self.cls, "school"))
        self.assertTrue(hasattr(self.cls, "phno"))
        self.assertTrue(hasattr(self.cls, "name"))

    def testSave(self):
        """test save"""
        self.cls.save()
        self.assertTrue(hasattr(self.cls, "updated_at"))

    def testToJson(self):
        """test to json func"""
        self.assertTrue(type(self.cls.to_json()) is dict)

if __name__ == "__main__":
    unittest.main
