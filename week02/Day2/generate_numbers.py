import sys
from random import randint


def main():
    file = open(sys.argv[1], 'w')

    for i in range(0, int(sys.argv[2])):
        file.write(" " + str(randint(1, 100)))


if __name__ == '__main__':
        main()
