import sys


def main():
        file = open(sys.argv[1], 'r')
        print(file.read())
        file.close()

if __name__ == '__main__':
    main()
