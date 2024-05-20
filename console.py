#!/usr/bin/python3
"""
The console module for managing objects
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    The console class
    """
    prompt = "(hbnb) "
    command_dict = {'BaseModel': BaseModel, 'User': User,
                    'State': State, 'City': City,
                    'Amenity': Amenity, 'Place': Place,
                    'Review': Review}

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
            command = args[0].strip()
            if command not in self.command_dict:
                print("** class doesn't exist **")
            else:
                my_model = self.command_dict[command]()
                print(my_model.id)
                my_model.save()

    def do_show(self, *args):
        """ Prints the string representation of an instance based on the
class name and id\n"""
        if not args or args[0].strip() == "":
            print("** class name missing **")
        else:
            arguments = args[0].strip().split()
            if len(arguments) != 2:
                print("** instance id missing **")
            else:
                if arguments[0] in self.command_dict:
                    all_objects = storage.all()
                    instance_id = "{}.{}".format(arguments[0], arguments[1])
                    if instance_id in all_objects:
                        print(all_objects[instance_id])
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_update(self, *args):
        """Updates an instance based on the class name and id\n"""
        if not args or args[0].strip() == "":
            print("** class name missing **")
        else:
            arguments = args[0].strip().split()
            if arguments[0] not in self.command_dict:
                    print("** class doesn't exist **")
            else:
                if len(arguments) == 1:
                    print("** instance id missing **")
                elif len(arguments) == 2:
                    print("** attribute name missing **")
                elif len(arguments) == 3:
                    print("** value missing **")
                elif len(arguments) > 3:
                    all_objects = storage.all()
                    instance_id = "{}.{}".format(arguments[0],
                                                 arguments[1])
                    if instance_id not in all_objects:
                        print("** no instance found **")
                    else:
                        if len(arguments) >= 4:
                            all_objects[instance_id][arguments[2]] = \
                                arguments[3]
                            storage.save()

    def do_all(self, *args):
        """Prints all string representation of all instances based or not
on the class name\n"""
        all_objects = storage.all()
        arguments = args[0].strip().split()
        if len(arguments) == 0:
            print(all_objects)
        elif len(arguments) == 1:
            if arguments[0] in self.command_dict:
                objects_of_class = {
                    key: all_objects[key] for key in all_objects
                    if all_objects[key]['__class__'] == arguments[0]
                }
                print(objects_of_class)
            else:
                print("** class doesn't exist **")

    def do_destroy(self, *args):
        """Destroys an object\n"""
        if not args or args[0].strip() == "":
            print("** class name missing **")
        else:
            arguments = args[0].strip().split()
            if len(arguments) != 2:
                print("** instance id missing **")
            else:
                if arguments[0] in self.command_dict:
                    all_objects = storage.all()
                    instance_id = "{}.{}".format(arguments[0], arguments[1])
                    if instance_id in all_objects:
                        del all_objects[instance_id]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

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

    def default(self, line):
        if not line.strip():
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
