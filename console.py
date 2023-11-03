#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """ hbnb command interpreter """
    prompt = '(hbnb) '
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Review': Review,
        'Amenity': Amenity,
        'Place': Place
        }

    def do_EOF(self, arg):
        """ End of file"""
        return True

    def do_quit(self, arg):
        """ exit the program"""
        return True

    def emptyline(self):
        """don´t execute nothing """
        pass

    def do_create(self, arg):
        """creates an instance of a class"""
        arguments_list = shlex.split(arg)
        if len(arguments_list) == 0:
            print('** class name missing **')
            return
        try:
            dummy = eval(arguments_list[0])()
            dummy.save()
            print(dummy.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                print(storage.all()["{}.{}".format(args[0], args[1])])
            except Exception as e:
                print("** no instance found **")
                pass

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        for key, value in storage.all().items():
            if args[1] == value.id:
                del storage.all()[key]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        """ Prints all str representation of all instances """
        argl = shlex.split(args)
        if len(args) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, args):
        """ Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        args = shlex.split(args)
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            obj_value = obj_dict[args[0] + "." + args[1]]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) == 2:
            for key, value in obj_dict.items():
                if value.id == args[1]:
                    print("** attribute name missing **")
                    return
            print("** no instance found **")
            return
        if len(args) == 3:
            type(eval(args[2])) != dict
            print("** value missing **")
            return

        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
