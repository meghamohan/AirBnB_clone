#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "
        """print("{}".format(cmd.Cmd.__dict__)) """

    def do_greet(self, line):
        print ("hello")

    def do_test(self, line):
        print ("testing...")

    def emptyline(self):
        return False

    def do_EOF(self, line):
        return True
    def do_eof(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
