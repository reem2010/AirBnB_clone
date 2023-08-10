#!/usr/bin/python3
"""Importing CMD"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
