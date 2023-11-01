#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ hbnb command interpreter """
    prompt = '(hbnb) '
    __classes = {'BaseModel': BaseModel}

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
        if len(arg) == 0:
            print("** class name missing **")
        elif arg == "BaseModel":
            obj = BaseModel()
            print(obj.id)
            obj.save()
        else:
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
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        for k, v in storage.all().items():
            if args[1] == v.id:
                del storage.all()[k]
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
