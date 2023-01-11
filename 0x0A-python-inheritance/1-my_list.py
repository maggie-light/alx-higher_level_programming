#!/usr/bin/python3
"""Define an inherited list class Mylist."""

class MyList(list):
    """implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """print a list in sorted ascending order."""
        print(sorted(self))

