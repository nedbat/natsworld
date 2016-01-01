"""Utils.py"""


class IndexLoop:
    """
    Create a sequence that returns the elements and their indices.
    Use like:
        for i, e in IndexLoop(list):
    """
    def __init__ (self, list):
        self.list = list

    def __getitem__ (self, index):
        return index, self.list [index]
