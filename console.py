#!/usr/bin/python3
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for AirBnB Console
    """
    prompt = "(hbnb) "
    cls = ["BaseModel", "User", "Review", "Place", "Amenity", "City", "State"]

    def do_greet(self, line):
        """ greet """
        print ("hello")

    def emptyline(self):
        """ accept empty lines """
        return False

    def do_EOF(self, line):
        """ EOF command """
        return True

    def do_quit(self, line):
        """ quit command """
        return True

    def do_create(self, line):
        """
        Create a new instance of BaseModel,
        save it (to JSON), prints id
        """
        args = line.split(' ')
        if (len(args) < 1):
            print("** class name missing **")
        elif args[0] not in HBNBCommand.cls:
                print("** class doesn't exist **")
        else:
            if args[0] in HBNBCommand.cls:
                if args[0] == "BaseModel":
                    newModel = BaseModel()
                if args[0] == "User":
                    newModel = User()
                if args[0] == "State":
                    newModel = State()
                if args[0] == "City":
                    newModel = City()
                if args[0] == "Amenity":
                    newModel = Amenity()
                if args[0] == "Place":
                    newModel = Place()
                if args[0] == "Review":
                    newModel = Review()
                newModel.save()
                print(newModel.id)

    def do_show(self, line):
        """
        Prints string representation of an instance
        based on class name/id
        """
        args = line.split(' ')
        if args[0] is None:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            myId = args[0] + '.' + args[1]
            found = False
            for key in objs:
                if myId == key:
                    found = True
                    print(objs[myId])
            if not found:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class
        name and id
        """
        args = line.split(' ')
        if len(args) < 2:
            print("** class name missing **")
        else:
            if args[0] in self.cls:
                storage.reload()
                myDict = storage.all()
                myId = args[0] + '.' + args[1]
                if myId in myDict.keys():
                    del myDict[myId]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        args = line.split(' ')
        if len(args) < 4:
            if len(args) == 0:
                print("** class name missing **")
            if len(args) == 1:
                print("** instance id missing **")
            if len(args) == 2:
                print("** value missing **")
            if len(args) == 3:
                print("** value missing **")
        else:
            argCls = args[0]
            argId = args[1]
            argId = argCls + '.' + argId
            attrName = args[2]
            if self.is_number(args[3]):
                attrValue = int(args[3].replace('\"', ''))
            else:
                attrValue = args[3].replace('\"', '')
            storage.reload()
            myDict = storage.all()
            if argCls in self.cls:
                if argId in myDict:
                    myNewObj = myDict[argId]
                    setattr(myNewObj, attrName, attrValue)
                    myNewObj.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all instances of an object
        Can be called directly or through object type
        """
        args = line.split()
        if len(args) > 0:
            if args[0] in self.cls:
                storage.reload()
                myDict = storage.all()
                for key in myDict.keys():
                    if args[0] in key.split('.'):
                        print(myDict[key])
            else:
                print("** class doesn't exist **")
        else:
            storage.reload()
            myDict = storage.all()
            for key in myDict.keys():
                print(myDict[key])

    def is_number(self, s):
        """ helper function to check if the value 's' is a
        number or not"""
        try:
            int(s)
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
