import sys


def main():
    sum_ = 0
    file = open(sys.argv[1], 'r')

    temp = [[int(i) for i in lines.split()] for lines in file]
    file.close()

    for i in temp:
        sum_ += sum(i)

    print(sum_)

if __name__ == '__main__':
    main()
