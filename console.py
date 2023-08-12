#!/usr/bin/python3
"""Importing CMD"""
import cmd
from models.base_model import BaseModel
from models import storage


def valid_key(command):
    """return valid key to the dictionary"""
    classs = [BaseModel.__name__]
    valid_key = ""
    if len(command) == 0:
        print("** class name missing **")
    elif command[0] not in classs:
        print("** class doesn't exist **")
    elif len(command) == 1:
        print("** instance id missing **")
    else:
        key = f"{command[0]}.{command[1]}"
        dict1 = storage.all().copy()
        if key not in dict1:
            print("** no instance found **")
        else:
            valid_key = key
    return(valid_key)


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
        """Create a new instance of BaseModel"""
        classs = [BaseModel]
        if len(line) == 0:
            print("** class name missing **")
            return
        for model in classs:
            if model.__name__ == line:
                obj = model()
                obj.save()
                print(obj.id)
                return
        print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of
        an instance based on the class name
        """
        command = line.split()
        key = valid_key(command)
        if len(key) != 0:
            dict1 = storage.all()
            obj = dict1[key]
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        command = line.split()
        key = valid_key(command)
        if len(key) != 0:
            dict1 = storage.all()
            obj = dict1[key]
            del obj
            del dict1[key]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of
        all instances based or not on the class name
        """
        models = [BaseModel.__name__]
        out = []
        if len(line) != 0 and line not in models:
            print("** class doesn't exist **")
        else:
            dict1 = storage.all()
            print(dict1)
            for key in dict1.keys():
                if len(line) == 0 or key.split('.')[0] == line:
                    out.append((dict1[key]).__str__())
            print(out)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        command = line.split()
        key = valid_key(command)
        if len(key) == 0:
            return
        if len(command) == 2:
            print("** attribute name missing **")
        elif len(command) == 3:
            print("** value missing **")
        else:
            if command[3].isdigit():
                command[3] = int(command[3])
            elif '\"' in command[3]:
                command[3] = command[3].replace("\"", "")
            else:
                command[3] = float(command[3])
            dict1 = storage.all()
            obj = dict1[key]
            setattr(obj, command[2], command[3])
            dict1[key] = obj
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
