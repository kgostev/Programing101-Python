import sys


def main():
    for arg in sys.argv[1:]:
        file = open(arg, 'r')
        print(file.read())
        file.close()

if __name__ == '__main__':
    main()
