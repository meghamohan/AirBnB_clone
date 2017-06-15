#!/usr/bin/python3
import unittest
from models.user import User


class UserTest(unittest.TestCase):
    """ unittest for BaseModel class"""
    def setUp(self):
        """ create a new instance """
        self.cls = User()

    def testType(self):
        """test for type"""
        self.assertEqual(self.cls.__class__.__name__, "User")

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
        self.assertEqual(self.cls.email, "")
        self.assertEqual(self.cls.password, "")
        self.assertEqual(self.cls.first_name, "")
        self.assertEqual(self.cls.last_name, "")
        self.cls.email = "119@holbertonschool.com"
        self.cls.password = "holberton"
        self.cls.first_name = "Hbtn"
        self.cls.last_name = "Hbtn"
        self.assertEqual(self.cls.email, "119@holbertonschool.com")
        self.assertEqual(self.cls.password, "holberton")
        self.assertEqual(self.cls.first_name, "Hbtn")
        self.assertEqual(self.cls.last_name, "Hbtn")

    def testSave(self):
        """test for save func"""
        self.cls.save()
        self.assertTrue(hasattr(self.cls, "updated_at"))

    def testToJson(self):
        """test for json"""
        self.assertTrue(type(self.cls.to_json()) is dict)

if __name__ == "__main__":
    unittest.main
