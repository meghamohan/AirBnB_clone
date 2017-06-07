#!/usr/bin/python3
""" Base model """

from datetime import datetime, date, time
from uuid import uuid4

class BaseModel:
    """ defining BaseModel class """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_json(self):
        newDict = self.__dict__.copy()
        newDict.update({'__class__': self.__class__.__name__})
        newDict.update({'created_at': str(self.created_at)})
        newDict.update({'updated_at': str(self.updated_at)})
        return (newDict)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                 self.id, self.__dict__))
