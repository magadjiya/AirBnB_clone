#!/usr/bin/python3
"""
The console module for managing objects
"""
from cmd import Cmd
import sys


class TheConsole(Cmd):
    """
    The console class
    """
    prompt = "(hbnb) "

    def precmd(self, line):
        if line != 'EOF':
            line = line.lower()
        return line

    def do_create(self):
        """
        Creates an object
        """
        pass

    def do_retrieve(self, obj):
        """
        Retrieves an object from a file/database
        """
        pass

    def do_destroy(self):
        """
        Destroys an object
        """
        pass

    def do_quit(self, line):
        """
        Exits console
        """

        self.postcmd(True, line)

    def postcmd(self, stop, line):
        if line.strip() == 'quit':
            sys.exit()
        return stop

    def do_EOF(self, line):
        """
        Exits console when EOF is returned
        """
        return True

    def postloop(self):
        print()


if __name__ == '__main__':
    TheConsole().cmdloop()
