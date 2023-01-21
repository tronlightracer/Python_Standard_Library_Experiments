from itertools import combinations, chain

def main():
    items = ["A", "b", "C"]
    more_items = ["e", "F", "g"]
    print(list(combinations(chain(items, more_items), 3)))

if __name__ == '__main__':
    main()