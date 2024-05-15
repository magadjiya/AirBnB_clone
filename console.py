#!/usr/bin/python3
"""
The console module for managing objects
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    The console class
    """
    prompt = "(hbnb) "

    def precmd(self, line):
        exemptions = ['EOF', 'help EOF']
        for line in exemptions:
            if not line:
                line = line.lower()
        return line

    def do_create(self, obj):
        """Creates an object\n"""
        pass

    def do_retrieve(self, obj):
        """Retrieves an object from a file/database\n"""
        pass

    def do_destroy(self, obj):
        """Destroys an object\n"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program\n"""

        self.postcmd(True, line)

    def postcmd(self, stop, line):
        if line.strip() == 'quit':
            sys.exit()
        return stop

    def do_EOF(self, line):
        """Exits console: Ctrl-D\n"""
        return True

    def postloop(self):
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
