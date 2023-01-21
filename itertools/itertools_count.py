from itertools import count

def main():
    for i in count(60):
        print(i)
        if i == 121:
            break


if __name__ == '__main__':
    main()