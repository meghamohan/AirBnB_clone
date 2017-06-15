#!/usr/bin/python3
import unittest
from models.review import Review


class ReviewTest(unittest.TestCase):
    """ unittest for BaseModel class"""
    def setUp(self):
        """ create a new instance """
        self.cls = Review()

    def testType(self):
        """test for class type"""
        self.assertEqual(self.cls.__class__.__name__, "Review")

    def testAttributes(self):
        """test for attributes"""
        self.assertTrue(hasattr(self.cls, "id"))
        self.assertTrue(hasattr(self.cls, "created_at"))
        self.assertFalse(hasattr(self.cls, "updated_at"))
        self.assertFalse(hasattr(self.cls, "Holberton"))
        self.cls.school = "Holberton"
        self.cls.phno = 408505
        self.assertTrue(hasattr(self.cls, "school"))
        self.assertTrue(hasattr(self.cls, "phno"))
        self.assertTrue(hasattr(self.cls, "text"))
        self.assertEqual(self.cls.__class__.__name__, "Review")
        self.assertEqual(self.cls.text, "")

    def testSave(self):
        """test for Save"""
        self.cls.save()
        self.assertTrue(hasattr(self.cls, "updated_at"))

    def testToJson(self):
        """test for json"""
        self.assertTrue(type(self.cls.to_json()) is dict)

if __name__ == "__main__":
    unittest.main
