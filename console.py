#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ hbnb command interpreter """
    prompt = '(hbnb) '
    __classes = {'BaseModel': BaseModel, 'User': User}

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
        arguments_list = arg.split()
        if len(arguments_list) == 0:
            print('** class name missing **')
            return
        try:
            dummy = eval(arguments_list[0])()
            dummy.save()
            print(dummy.id)
        except:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in __classes:
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if args[1] == value.id:
                del storage.all()[key]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        """ Prints all str representation of all instances """
        argl = args.split()
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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
