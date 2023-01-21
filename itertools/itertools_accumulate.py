from itertools import accumulate

def main():
    """
    accumulate(range(1, 10)) will add each number of the index of the range to the previous value
    returns 1, 3, 6, 10, 15, 21, 28, 36, 45
            1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 == 45

    """
    for i in accumulate(range(1, 10)):
        print(i)

if __name__ == '__main__':
    main()