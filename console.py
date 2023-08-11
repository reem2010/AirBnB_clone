#!/usr/bin/python3
"""Importing CMD"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Inheritance of cmd class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """To exit the program"""
        return True

    def do_quit(self, line):
        """To quit the program"""
        return True

    def emptyline(self):
        return

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        classs = [BaseModel]
        line = line.replace("\n", "")
        if len(line) == 0:
            print("** class name missing **")
            return
        for model in classs:
            if model.__name__ == line:
                model().save()
                return
        print("** class doesn't exist **")

    def do_show(self, line):
        classs = [BaseModel]
        found = 0;
        line = line.replace("\n", "")
        if len(line) == 0:
            print("** class name missing **")
            return
        command = line.split()
        for model in classs:
            if model.__name__ == command[0]:
                found = 1
        if (found == 0):
            print("** class doesn't exist **")
            return
        if len(command) == 1:
            print("** instance id missing **")
            return
        dict1 = storage.all()
        key = f"{command[0]}.{command[1]}"
        if key not in dict1:
            print ("** no instance found **")
        else:
            obj = dict1[key]
            print(obj)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
