#!/usr/bin/python3
"""
The console module for managing objects
"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    The console class
    """
    prompt = "(hbnb) "

    def precmd(self, line):
        exemptions = ['EOF', 'help EOF']
        for exempt in exemptions:
            if not exempt:
                line = line.lower()
        return line

    def do_create(self, *args):
        """Creates an object\n"""
        if not args or args[0].strip() == "":
            print("** class name missing **")
        else:
            command_dict = {'BaseModel': BaseModel, 'User': User}
            command = args[0].strip()
            if command not in command_dict:
                print("** class doesn't exist **")
            else:                      
                my_model = command_dict[command]()
                my_model.save()
            
    def do_show(self, *args):
        """ Prints the string representation of an instance based on the
class name and id\n"""
        pass

    def do_update(self, *args):
        """Updates an instance based on the class name and id\n"""
        pass

    def do_all(self, *args):
        """Prints all string representation of all instances based or not
on the class name\n"""
        pass

    def do_retrieve(self, *args):
        """Retrieves an object from a file/database\n"""
        pass

    def do_destroy(self, *args):
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
