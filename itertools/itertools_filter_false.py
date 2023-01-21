from itertools import filterfalse

def falsey():
    print(list(filterfalse(lambda x: x % 2 == 1, range(10))))

if __name__ == '__main__':
    falsey()