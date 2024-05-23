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
        """Executes when the console is started\n"""
        exemptions = ['EOF', 'help EOF']
        for exempt in exemptions:
            if not exempt:
                line = line.lower()
        return line

    def do_create(self, args):
        """Creates an object\n"""
        if not args or args[0].strip() == "":
            print("** class name missing **")
        else:
            command = args.strip()
            if command not in self.command_dict:
                print("** class doesn't exist **")
            else:
                my_model = self.command_dict[command]()
                print(my_model.id)
                my_model.save()

    def do_show(self, args):
        """ Prints the string representation of an instance based on the
class name and id\n"""
        if args is None or args.strip() == "":
            print("** class name missing **")
        else:
            args = args.split()
            class_name = args[0]
            if class_name not in self.command_dict:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    id_str = args[1]
                    all_objects = storage.all()
                    instance_id = "{}.{}".format(class_name, id_str)
                    if instance_id in all_objects:
                        print(all_objects[instance_id])
                    else:
                        print("** no instance found **")

    def do_update(self, args):
        """Updates an instance based on the class name and id\n"""
        if not args or args.strip() == "":
            print("** class name missing **")
        else:
            args = args.split()
            class_name = args[0]
            if class_name not in self.command_dict:
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                elif len(args) >= 4:
                    all_objects = storage.all()
                    instance_id = "{}.{}".format(class_name,
                                                 args[1])
                    if instance_id not in all_objects:
                        print("** no instance found **")
                    else:
                        obj = storage.all()[instance_id]
                        if len(args) == 4:
                            attr_name = args[2]
                            attr_value = args[3]
                            setattr(obj, attr_name, attr_value)
                            obj.save()
                        elif len(args) > 4:
                            attr_dict = {}
                            for i in range(2, len(args), 2):
                                attr_name = args[i]
                                attr_value = args[i+1]
                                attr_dict[attr_name] = attr_value
                            obj.update(attr_dict)
                            obj.save
                        else:
                            attr_dict = eval(args[2])
                            obj.update(attr_dict)
                            obj.save()


    def do_all(self, class_name):
        """Prints all string representation of all instances based or not
on the class name\n"""
        all_objects = storage.all()
        if class_name is None or class_name.strip() == "":
            print(all_objects)
        elif class_name not in self.command_dict:
            print("** class doesn't exist **")
        else:
            class_name = class_name.strip()
            objects_of_class = {
                key: all_objects[key] for key in all_objects
                if all_objects[key]['__class__'] == class_name
            }
            print(objects_of_class)

    def do_destroy(self, args):
        """Destroys an object\n"""
        if not args or args.strip() == "":
            print("** class name missing **")
        else:
            args = args.split()
            class_name = args[0]
            if args[1] is None:
                print("** instance id missing **")
            else:
                id_str = args[1]
                if class_name in self.command_dict:
                    all_objects = storage.all()
                    instance_id = "{}.{}".format(class_name, id_str)
                    if instance_id in all_objects:
                        del all_objects[instance_id]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_count(self, class_name):
        all_objects = storage.all()
        count = sum(1 for obj in all_objects.values() if obj['__class__'] == class_name)
        print(count)

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        self.postcmd(True, line)

    def postcmd(self, stop, line):
        """Exits the console\n"""
        if line.strip() == 'quit':
            sys.exit()
        return stop

    def do_EOF(self, line):
        """Exits console: Ctrl-D\n"""
        return True

    def postloop(self):
        """Executes before console exits\n"""
        print()

    def emptyline(self):
        """Do nothing on empty input line\n"""
        pass

    def default(self, line):
        """Handles default behaviour of console\n"""
        line = line.strip()
        if '.' in line:
            class_name, command_with_id = line.split('.', 1)
            if '(' in command_with_id and ')' in command_with_id:
                command, id_str = command_with_id.split('(', 1)
                id_str = id_str.rstrip(')')
                if class_name in self.command_dict:
                    if command == 'all':
                        self.do_all(class_name)
                    elif command == 'count':
                        self.do_count(class_name)
                    elif command == 'show':
                        self.do_show("{} {}".format(class_name, id_str))
                    elif command == 'destroy':
                        self.do_destroy("{} {}".format(class_name, id_str))
                    elif command == 'update':
                        self.do_update("{} {}".format(class_name, id_str))
        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
