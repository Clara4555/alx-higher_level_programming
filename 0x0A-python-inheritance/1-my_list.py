#!/usr/bin/python3
class MyList(list):
    """sorting for  built-in list class."""
    def print_sorted(self):
        """prints sorted ascending order."""
        print(sorted(self))
