#!/usr/bin/python3
"""Importing CMD"""
import cmd
import re
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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
        """Enter and I will do nothing!"""

        return

    def do_create(self, line):
        """Create a new instance of BaseModel"""

        classs = [BaseModel, User, State, City, Amenity, Place]
        classs.append(Review)
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
        """Prints the string representation of an instance"""

        classs = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place']
        classs.append('Review')
        command = line.split()
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
                obj = dict1[key]
                print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        classs = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place']
        classs.append('Review')
        command = line.split()
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in classs:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        else:
            key = f"{command[0]}.{command[1]}"
            dict1 = storage.all()
            if key not in dict1:
                print("** no instance found **")
            else:
                obj = dict1[key]
                del obj
                del dict1[key]
                storage.save()

    def do_all(self, line):
        """representation of all instances based or not on the class name"""

        models = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place']
        models.append('Review')
        out = []
        if len(line) != 0 and line not in models:
            print("** class doesn't exist **")
        else:
            dict1 = storage.all()
            for key in dict1.keys():
                if len(line) == 0 or key.split('.')[0] == line:
                    out.append((dict1[key]).__str__())
            print(out)

    def default(self, line):
        """for unique syntax"""

        classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place']
        classes.append('Review')
        args = line.split('.')
        if len(args) == 2:
            A0 = args[0]
            A1 = args[1]
            if A0 not in classes:
                print("** class doesn't exist **")
            elif A1 == "all()":
                self.class_all(A0)
            elif A1 == "count()":
                self.count(A0)
            elif re.match(r"show", A1):
                pattern = str((re.search(r'"([^"]*)"', A1)).group())
                pattern = pattern.replace("\"", "")
                self.do_show(f"{A0} {pattern}")
            elif re.match(r"destroy", A1):
                pattern = str((re.search(r'"([^"]*)"', A1)).group())
                pattern = pattern.replace("\"", "")
                self.do_destroy(f"{A0} {pattern}")
            elif re.match(r"update", A1):
                self.do_dic(A0, A1)
        else:
            print('*** Unknown syntax:', line)

    def do_dic(self, A0, A1):
        """Update from dictionary"""
        pattern = (A1[A1.find('(')+1:A1.find(')')]).split(", ", 1)
        if not(re.match(r"^{", pattern[1])):
            pattern = (A1[A1.find('(')+1:A1.find(')')]).split(", ")
            pattern[0] = pattern[0].replace("\"", "")
            pattern[1] = pattern[1].replace("\"", "")
            pattern = f"{A0} {pattern[0]} {pattern[1]} {pattern[2]}"
            self.do_update(pattern)
        else:
            pattern[0] = pattern[0].replace("\"", "")
            pattern[1] = eval(pattern[1])
            for key, value in pattern[1].items():
                if type(value) == str:
                    patt = f"{A0} {pattern[0]} {key} \"{value}\""
                else:
                    patt = f"{A0} {pattern[0]} {key} {value}"
                self.do_update(patt)

    def class_all(self, args):
        """same as do_all"""
        dict1 = storage.all()
        out = []
        for key in dict1.keys():
            if key.split('.')[0] == args:
                out.append((dict1[key]).__str__())
        print(f"[{', '.join(out)}]")

    def count(self, args):
        """retrieve the number of instances of a class"""

        count = 0
        dict1 = storage.all().copy()
        for key in dict1.keys():
            if key.split('.')[0] == args:
                count += 1
        print(count)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""

        classs = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place']
        classs.append('Review')
        command = line.split()
        key = ""
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in classs:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        else:
            key1 = f"{command[0]}.{command[1]}"
            dict_1 = storage.all().copy()
            if key1 not in dict_1:
                print("** no instance found **")
            else:
                key = key1
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
