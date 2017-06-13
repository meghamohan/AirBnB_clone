#!/usr/bin/python3
""" FileStorage class """


import json
import os


class FileStorage:
    """ contains methods to serialize objects to JSON
    and to deserialize JSON files to objects """

    __file_path = './file.json'
    __objects = {}

    def all(self):
        """ returns __objects """
        return (self.__objects)

    def new(self, obj):
        """ sets in __objects the obj with key:
         <obj class name>.id """
        self.__objects[type(obj).__name__ + '.' + obj.id] = obj

    def save(self):
        """ serializes __objects to the JSON
         file (path: __file_path) """
        json_dict = {}
        for key in self.__objects.keys():
            json_dict[key] = self.__objects[key].to_json()
        with open(self.__file_path, 'w', encoding='utf8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """ deserializes the JSON file to __objects
         (only if the JSON file exists ;
         otherwise, do nothing)
         key => <obj class name>.id
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode='r+') as f:
                jsonObj = json.load(f)
                for key in jsonObj.keys():
                    className = key.split('.')[0]
                    """self.__objects[key] = exec(className)(**jsonObj[key])"""
                    if className in 'BaseModel':
                        from models.base_model import BaseModel
                        self.__objects[key] = BaseModel(**jsonObj[key])
                    if className in 'User':
                        from models.user import User
                        self.__objects[key] = User(**jsonObj[key])
                    if className in 'State':
                        from models.state import State
                        self.__objects[key] = State(**jsonObj[key])
                    if className in 'City':
                        from models.city import City
                        self.__objects[key] = City(**jsonObj[key])
                    if className in 'Amenity':
                        from models.amenity import Amenity
                        self.__objects[key] = Amenity(**jsonObj[key])
                    if className in 'Place':
                        from models.place import Place
                        self.__objects[key] = Place(**jsonObj[key])
                    if className in 'Review':
                        from models.review import Review
                        self.__objects[key] = Review(**jsonObj[key])
        else:
            self.__objects = {}
