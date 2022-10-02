"""
Basic implimentation of a data structure that I dont really know the name of.

This data structure contains cells, which are appended to the middle as either even or odd. The first thing appended will be even, the second odd. They are popped
either even or odd, and will either pop from the top or bottom depending upon it.


Marley Akins 2022 (C) MIT License
"""

import sys

class Structure(object):
    """
      [a, b, | c, d].push(f) -> [a, b, f, |  d, c]
    """
    def __init__(self):
        self.list = []
        self.even_top = False

    def push(self, value):
        if self.even_top:
            self.list.insert(len(self.list)//2, value)
        else:
            self.list.insert(len(self.list)//2+1, value)
        
        self.even_top = not self.even_top
        return self.list.index(value)

    def pop(self, top=True):
        if top:
            if self.even_top:
                return self.list.pop(0)
            else:
                return self.list.pop(-1)
        else:
            if self.even_top:
                return self.list.pop(-1)
            else:
                return self.list.pop(0)

    def __getitem__(self, key):
        return self.list[key]

    def __len__(self):
        return len(self.list)

    def __setitem__(self, key, value):
        self.list[key] = value

    def __str__(self):
        return str(self.list)

    def __iter__(self):
        return iter(self.list)

    def __reversed__(self):
        return reversed(self.list)

    def __contains__(self, item):
        return item in self.list

    def __delitem__(self, key):
        del self.list[key]

    def __eq__(self, other):
        return self.list == other.list

    def __ne__(self, other):
        return self.list != other.list
