#!/usr/bin/python3
import unittest
from models.place import Place


class PlaceTest(unittest.TestCase):
    """ unittest for BaseModel class"""
    def setUp(self):
        """ create a new instance """
        self.cls = Place()

    def testType(self):
        """tetsing type"""
        self.assertEqual(self.cls.__class__.__name__, "Place")

    def testAttributes(self):
        """testing all attribute functionality"""
        self.assertTrue(hasattr(self.cls, "id"))
        self.assertTrue(hasattr(self.cls, "created_at"))
        self.assertFalse(hasattr(self.cls, "updated_at"))
        self.assertFalse(hasattr(self.cls, "Holberton"))
        self.cls.school = "Holberton"
        self.cls.phno = 408505
        self.assertTrue(hasattr(self.cls, "school"))
        self.assertTrue(hasattr(self.cls, "phno"))
        self.assertEqual(self.cls.city_id, "")
        self.assertEqual(self.cls.user_id, "")
        self.assertEqual(self.cls.name, "")
        self.assertEqual(self.cls.description, "")
        self.assertEqual(self.cls.number_rooms, 0)
        self.assertEqual(self.cls.number_bathrooms, 0)
        self.assertEqual(self.cls.max_guest, 0)
        self.assertEqual(self.cls.price_by_night, 0)
        self.assertEqual(self.cls.latitude, 0.0)
        self.assertEqual(self.cls.longitude, 0.0)
        self.assertEqual(self.cls.amenities, [])

    def testSave(self):
        """save test"""
        self.cls.save()
        self.assertTrue(hasattr(self.cls, "updated_at"))

    def testToJson(self):
        """json test"""
        self.assertTrue(type(self.cls.to_json()) is dict)

    def teststr(self):
        """testing str function"""
        print1 = "[{}] ({}) {}".format(self.cls.__class__.__name__,
                                       str(self.cls.id),
                                       self.cls.__dict__)
        self.assertEqual(print(print1), print(self.cls))

if __name__ == "__main__":
    unittest.main
