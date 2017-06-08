#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import *
import json

class HBNBCommand(cmd.Cmd):
    """ def __init__(self):"""
    """   cmd.Cmd.__init__(self)"""
    prompt = "(hbnb) "
    cls = ["BaseModel", "User"]



    def do_greet(self, line):
        print ("hello")

    def do_test(self, line):
        print ("testing...")

    def emptyline(self):
        return False

    def do_EOF(self, line):
        return True
    def do_quit(self, line):
        return True


    def do_create(self, line):
        """Create a new instance of BaseModel, save it (to JSON), prints id"""
        args = line.split(' ')
        print(args)
        if (len(args) < 1):
            print("** class name missing **")
        elif args[0] not in HBNBCommand.cls:
                print("** class doesn't exist **")
        else:
             if args[0] in HBNBCommand.cls:
                if args[0] == "BaseModel":
                    newModel = BaseModel()
                newModel.save()
                print(newModel.id)

    def do_show(self, line):
        args = line.split(' ')
        if args[0] is None:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            myId = args[1]
            print(myId)
            if myId in objs.keys():
                print(objs[myId])
            else:
                print("** no instance found **")


    def do_destroy(self, line):
        pass


    def do_update(self, line):
        pass


    def do_all(self, line):
        """
        Prints all instances of an object
        Can be called directly or through object type
        """
        args = line.split()
        if len(args) > 1:
            if args[0] in self.cls:
                storage.reload()
                myDict = storage.all()
                for key in myDict.keys():
                    if args[0] in str(myDict[key]):
                        print(myDict[key])
            else:
                print("error!!")
        else:
            storage.reload()
            myDict = storage.all()
            for key in myDict.keys():
                print(myDict[key]) 


if __name__ == '__main__':
    HBNBCommand().cmdloop()
