#!/usr/bin/python3
import sys
import unittest
from unittest.mock import create_autospec
from test.support import captured_stdout, captured_stderr
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """class TestConsole"""
    def setUp(self):
        """setting up mock_stdin and mock_stdout"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        """creating HBNBCommand"""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_exit(self):
        """exit command"""
        tst = self.create()
        self.assertTrue(tst.onecmd("quit"))

    def test_EOF(self):
        """exit command"""
        tst = self.create()
        self.assertTrue(tst.onecmd("EOF"))

    def test_create(self):
        tst = self.create()
        self.assertFalse(tst.onecmd("create BaseModel"))
        self.assertEqual("** instance id missing **\n", stdout.getvalue())
        self.assertFalse(tst.onecmd("create"))
        self.assertEqual("** class name missing **\n", stdout.getvalue())
        self.assertFalse(tst.onecmd("create Holberton"))
        self.assertEqual("** class doesn't exist **\n", stdout.getvalue())
