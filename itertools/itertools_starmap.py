from itertools import starmap

def main():
    """
    itertools.starmap applies a function to each elements in a list of iterables
    """
    print(list(starmap(lambda x, y: x * y, [(2, 6), (8, 4), (5, 3)])))