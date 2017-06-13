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

    def emptyline(self):
        """ accept empty lines """
        return False

    def do_EOF(self, line):
        """ command to exit console """
        return True

    def do_quit(self, line):
        """ quit command """
        return True

    def do_create(self, line):
        """
        Create a new instance of BaseModel,
        save it (to JSON), prints id
        """
        args = line.split()
        if (len(args) == 0):
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
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        elif len(args) == 1:
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
        args = line.split()
        if len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 0:
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
        args = line.split()
        if len(args) < 4:
            if len(args) == 0:
                print("** class name missing **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** value missing **")
            elif len(args) == 3:
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
        count = 0
        if len(args) > 0:
            if args[0] in self.cls:
                storage.reload()
                myDict = storage.all()
                for key in myDict.keys():
                    if args[0] in key.split('.'):
                        print(myDict[key])
                        count += 1
                if count == 0:
                    print("[]")
            else:
                print("** class doesn't exist **")
        else:
            storage.reload()
            myDict = storage.all()
            for key in myDict.keys():
                print(myDict[key])

    def do_BaseModel(self, line):
        """does functions like all,count,show,update
        destroy"""
        if line == ".all()":
            self.do_all("BaseModel")
        elif line == ".count()":
            self.printCount("BaseModel")
        elif line[0:5] == ".show":
            print("BaseModel " + line[7:-2])
            self.do_show("BaseModel " + line[7:-2])
        elif line[0:8] == ".destroy":
            self.do_destroy("BaseModel " + line[10:-2])
        elif line[0:7] == ".update":
            self.do_update("BaseModel " + self.reconstructMyArg(line[8:-1]))

    def do_Place(self, line):
        """does functions like all,count,show,update
        destroy"""
        if line == ".all()":
            self.do_all("Place")
        elif line == ".count()":
            self.printCount("Place")
        elif line[0:5] == ".show":
            print("Place " + line[7:-2])
            self.do_show("Place " + line[7:-2])
        elif line[0:8] == ".destroy":
            self.do_destroy("Place " + line[10:-2])
        elif line[0:7] == ".update":
            self.do_update("Place " + self.reconstructMyArg(line[8:-1]))

    def do_User(self, line):
        """does functions like all,count,show,update
        destroy"""
        if line == ".all()":
            self.do_all("User")
        elif line == ".count()":
            self.printCount("User")
        elif line[0:5] == ".show":
            print("User " + line[7:-2])
            self.do_show("User " + line[7:-2])
        elif line[0:8] == ".destroy":
            self.do_destroy("User " + line[10:-2])
        elif line[0:7] == ".update":
            self.do_update("User " + self.reconstructMyArg(line[8:-1]))

    def do_State(self, line):
        """does functions like all,count,show,update
        destroy"""
        if line == ".all()":
            self.do_all("State")
        elif line == ".count()":
            self.printCount("State")
        elif line[0:5] == ".show":
            print("State " + line[7:-2])
            self.do_show("State " + line[7:-2])
        elif line[0:8] == ".destroy":
            self.do_destroy("State " + line[10:-2])
        elif line[0:7] == ".update":
            self.do_update("State " + self.reconstructMyArg(line[8:-1]))

    def do_Review(self, line):
        """does functions like all,count,show,update
        destroy"""
        if line == ".all()":
            self.do_all("Review")
        elif line == ".count()":
            self.printCount("Review")
        elif line[0:5] == ".show":
            print("Review " + line[7:-2])
            self.do_show("Review " + line[7:-2])
        elif line[0:8] == ".destroy":
            self.do_destroy(" " + line[10:-2])
        elif line[0:7] == ".update":
            self.do_update("Review " + self.reconstructMyArg(line[8:-1]))

    def do_Amenity(self, line):
        """does functions like all,count,show,update
        destroy"""
        if line == ".all()":
            self.do_all("Amenity")
        elif line == ".count()":
            self.printCount("Amenity")
        elif line[0:5] == ".show":
            print("Amenity " + line[7:-2])
            self.do_show("Amenity " + line[7:-2])
        elif line[0:8] == ".destroy":
            self.do_destroy("Amenity " + line[10:-2])
        elif line[0:7] == ".update":
            self.do_update("Amenity " + self.reconstructMyArg(line[8:-1]))

    def do_City(self, line):
        """does functions like all,count,show,update
        destroy"""
        if line == ".all()":
            self.do_all("City")
        elif line == ".count()":
            self.printCount("City")
        elif line[0:5] == ".show":
            print("City " + line[7:-2])
            self.do_show("City " + line[7:-2])
        elif line[0:8] == ".destroy":
            self.do_destroy("City " + line[10:-2])
        elif line[0:7] == ".update":
            self.do_update("City " + self.reconstructMyArg(line[8:-1]))

    def reconstructMyArg(self, arg):
        """ formats the args"""
        newArgs = arg.split()
        newArg0 = newArgs[0].replace('\"', '')
        newArg0 = newArg0.replace(',', '')
        newArg1 = newArgs[1].replace('\"', '')
        newArg1 = newArg1.replace('\'', '')
        newArg1 = newArg1.replace('{', '')
        newArg1 = newArg1.replace(':', '')
        newArg1 = newArg1.replace(',', '')
        newArg2 = newArgs[2].replace('\"', '')
        newArg2 = newArg2.replace('\'', '')
        newArg2 = newArg2.replace('{', '')
        newArg2 = newArg2.replace(':', '')
        newArg2 = newArg2.replace(',', '')
        """newArg3 = newArgs[3].replace('\"', '')
        newArg3 = newArg3.replace('\'', '')
        newArg3 = newArg3.replace(':', '')
        newArg3 = newArg3.replace(',', '')
        newArg4 = newArgs[4].replace('\"', '')
        newArg4 = newArg4.replace('\'', '')
        newArg4 = newArg4.replace('}', '')
        newArg4 = newArg4.replace(':', '')
        newArg4 = newArg4.replace(',', '')"""
        return (newArg0 + ' ' + newArg1 + ' ' + newArg2)

    def clsAll(self, arg):
        """prints all instances of a specific class"""
        myDict = storage.all()
        count = 0
        print(arg)
        for key in myDict.keys():
            if arg in key.split('.'):
                print(myDict[key])
                count += 1
        if count == 0:
            print("[]")

    def printCount(self, arg):
        """counts number of instances"""
        myDict = storage.all()
        count = 0
        for k in myDict.keys():
            obj = (myDict[k].__class__.__name__)
            if (obj == arg):
                count += 1
        print(count)

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
