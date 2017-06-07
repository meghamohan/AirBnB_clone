#!/usr/bin/python3
import json
import models
import os

""" FileStorage class """

class FileStorage:
    """ contains methods to serialize objects to JSON
    and to deserialize JSON files to objects """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns __objects """
        return (FileStorage.__objects)

    def new(self, obj):
        """ sets in __objects the obj with key
         <obj class name>.id """
        FileStorage.__objects[obj.id] = obj


    def save(self):
        """ serializes __objects to the JSON
         file (path: __file_path) """
        with open(self.__file_path, 'w', encoding='utf8') as f:
            f.write(json.dumps(self.__objects))


    def reload(self):
        """ deserializes the JSON file to __objects
         (only if the JSON file exists ;
         otherwise, do nothing) """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode ='r', encoding="utf8") as f:
                self.__objects = json.load(f)
