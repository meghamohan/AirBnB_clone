#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """ unittest for BaseModel class"""
    def setUp(self):
        """ create a new instance """
        self.cls = BaseModel()

    def testType(self):
        self.assertEqual(self.cls.__class__.__name__, "BaseModel")

    def testAttributes(self):
        self.assertTrue(hasattr(self.cls, "id"))
        self.assertTrue(hasattr(self.cls, "created_at"))
        self.assertFalse(hasattr(self.cls, "updated_at"))
        self.assertFalse(hasattr(self.cls, "Holberton"))
        self.cls.school = "Holberton"
        self.cls.phno = 408505
        self.assertTrue(hasattr(self.cls, "school"))
        self.assertTrue(hasattr(self.cls, "phno"))
        self.assertEqual(self.cls.school, "Holberton")
        self.assertEqual(self.cls.phno, 408505)

    def testSave(self):
        self.cls.save()
        self.assertTrue(hasattr(self.cls, "updated_at"))

    def testToJson(self):
        self.assertTrue(type(self.cls.to_json()) is dict)

    def test__str__(self):
        """method to test __str__ functionality"""
        print1 = "[{}] ({}) {}".format(self.cls.__class__.__name__,
                                       self.cls.id, self.cls.__dict__)
        self.assertEqual(print(self.cls), print(print1))

if __name__ == "__main__":
    unittest.main
