from itertools import permutations as perm

def main():
    # permutations shows all the possible combinations of items in a list
    for i in perm(["A", "B", "C"]):
        print(i)

if __name__ == '__main__':
    main()