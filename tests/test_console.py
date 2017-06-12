#!/usr/bin/python3
import sys
import unittest
from unittest.mock import create_autospec
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

    def test_quit(self):
        """ testing quit"""
        cmd = self.create()
        self.assertRaises(SystemExit, quit)

    def test_exit(self):
        """exit command"""
        tst = self.create()
        self.assertTrue(tst.onecmd("quit"))
