#!/usr/bin/python3
""" Base model class """
from datetime import datetime, date, time
from uuid import uuid4
import json
import models


class BaseModel:
    """ defining BaseModel class that defines all common
     attributes/methods for other classes:"""
    dateFormat = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """ function initialization """
        if kwargs:
            self.__dict__ = kwargs
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs.get('created_at'),
                                                    self.dateFormat)
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs.get('updated_at'),
                                                    self.dateFormat)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute updated_at
         with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_json(self):
        """
        returns a dictionary containing all keys/values of
         __dict__ of the instance + the class name in the key __class__.
         This method will be the first piece
         of the serialization/deserialization process
        """
        newDict = self.__dict__.copy()
        newDict.update({'__class__': self.__class__.__name__})
        newDict.update({'created_at': str(self.created_at.isoformat())})
        if hasattr(self, 'updated_at'):
            newDict.update({'updated_at': str(self.updated_at.isoformat())})
        return (newDict)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))
