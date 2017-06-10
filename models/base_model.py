#!/usr/bin/python3
""" Base model """

from datetime import datetime, date, time
from uuid import uuid4
import json
import models

class BaseModel:
    """ defining BaseModel class """
    dateFormat = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__ = kwargs
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs.get('created_at'), self.dateFormat)
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs.get('updated_at'), self.dateFormat)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_json(self):
        newDict = self.__dict__.copy()
        newDict.update({'__class__': self.__class__.__name__})
        newDict.update({'created_at': str(self.created_at.isoformat())})
        if hasattr(self, 'updated_at'):
            newDict.update({'updated_at': str(self.updated_at.isoformat())})
        return (newDict)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                 self.id, self.__dict__))
